# Packet Capture Project

This project demonstrates packet capturing using both a Python script and a Bash script. The Python file leverages Scapy for packet sniffing and storing data, while the Bash file uses `tcpdump` to capture packets and save them to a `.cap` file.


## Requirements

### Python Script Requirements
1. **Scapy**: A Python library for packet manipulation and analysis.
   - Install Scapy using pip:
     ```bash
     pip install scapy
     ```

### Bash Script Requirements
1. **tcpdump**: A network packet analyzer tool.
   - Install tcpdump using apt (for Debian-based systems):
     ```bash
     sudo apt install tcpdump
     ```

## Usage Instructions

1. **Python Packet Capture**:
   - Run the Python script:
     ```bash
     python3 capture_packets.py
     ```
   - The captured packets will be saved in the `captured_packets.cap` file.

2. **Bash Packet Capture**:
   - Make the Bash script executable:
     ```bash
     chmod +x capture_packets.sh
     ```
   - Run the script:
     ```bash
     ./capture_packets.sh
     ```
   - The captured packets will be saved in the `captured_packets.cap` file.
   - 

## Analyzing Captured Packets

After capturing the packets using either script, you can analyze the `.cap` file using tools like **Wireshark** or **tcpdump** itself.

For example, to analyze using Wireshark:
```bash
wireshark captured_packets.cap
```

Or with tcpdump:
```bash
tcpdump -r captured_packets.cap
```

