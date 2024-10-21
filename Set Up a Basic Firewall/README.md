
# Firewall Manager

This project includes two scripts for managing firewall rules: one written in Python and the other in Bash. The scripts enable you to configure firewall settings easily, allowing or blocking traffic on specified ports.

## Project Structure

```
.
├── firewall_manager.py  # Python script for managing firewall rules
└── firewall_setup.sh     # Bash script for setting up firewall rules
```

### Description

#### Python Script: `firewall_manager.py`
- **Purpose**: This script uses the `ufw` (Uncomplicated Firewall) to enable or disable the firewall and manage traffic rules.
- **Functionality**:
  - Enables the firewall.
  - Allows traffic on ports 80 (HTTP) and 443 (HTTPS).
  - Blocks traffic on port 21 (FTP).
  - Provides feedback for each operation.

#### Bash Script: `firewall_setup.sh`
- **Purpose**: This script uses `tcpdump` for packet capturing and can store the captured packets in a `.cap` file.
- **Functionality**:
  - Starts packet capture on all interfaces.
  - Stores captured packets in a specified `.cap` file for later analysis.

### Usage

#### Running the Python Script

1. Ensure `ufw` is installed on your system:
   ```bash
   sudo apt install ufw
   ```

2. Run the Python script:
   ```bash
   python3 firewall_manager.py
   ```

#### Running the Bash Script

1. Make the Bash script executable:
   ```bash
   chmod +x firewall_setup.sh
   ```

2. Run the Bash script:
   ```bash
   ./firewall_setup.sh
   ```

### Dependencies

- Python 3
- UFW (Uncomplicated Firewall)
- tcpdump (for packet capturing)

### Notes

- Ensure you have the necessary permissions to run these scripts (e.g., using `sudo`).
- Modify the scripts as needed to suit your firewall rules or packet capturing preferences.
