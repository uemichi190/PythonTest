import pyshark

file_path = 'sample.pcap'

try:
    cap = pyshark.FileCapture(file_path)
    print(f"Opened capture file: {file_path}")

    # Iterate through the packets
    for packet in cap:
        # Print a basic summary of the packet
        print(f"Packet No. {packet.number}: {packet.length} bytes, Protocol: {packet.highest_layer}")
        # You can access specific layers and fields, for example:
        # print(f"  Source IP: {packet.ip.src} -> Destination IP: {packet.ip.dst}")
        
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # It's good practice to close the capture object to free resources
    if 'cap' in locals() and cap:
        cap.close()

