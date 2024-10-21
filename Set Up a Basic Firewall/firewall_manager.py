import subprocess

def run_command(command):
    """Run a system command and return the output."""
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return f"Command failed: {e.output.decode('utf-8')}"

def enable_firewall():
    print("Enabling firewall...")
    result = run_command("sudo ufw enable")
    print(result)

def disable_firewall():
    print("Disabling firewall...")
    result = run_command("sudo ufw disable")
    print(result)

def allow_port(port):
    print(f"Allowing traffic on port {port}...")
    result = run_command(f"sudo ufw allow {port}")
    print(result)

def block_port(port):
    print(f"Blocking traffic on port {port}...")
    result = run_command(f"sudo ufw deny {port}")
    print(result)

if __name__ == "__main__":
    print("Firewall Manager\n")
    
    # Example usage
    enable_firewall()
    allow_port(80)  # Allow HTTP
    allow_port(443)  # Allow HTTPS
    block_port(21)  # Block FTP
    disable_firewall()  # Disable firewall (for testing purposes)
