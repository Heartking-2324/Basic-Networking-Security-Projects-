from scapy.all import sniff, wrpcap

# Callback function to handle each packet
def packet_callback(packet):
    print(packet.summary())  # Print a summary of each packet

# Main function to start packet capture and save to .cap file
if __name__ == "__main__":
    print("Starting packet capture...")

    # Capture packets and store them in a list
    packets = sniff(prn=packet_callback, store=True, count=100)  # Modify count or add filters as needed

    # Save captured packets to a .cap file
    wrpcap("captured_packets.cap", packets)

    print("Packet capture complete. Data saved in 'captured_packets.cap'.")
