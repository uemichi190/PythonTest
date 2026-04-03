<<<<<<< HEAD
#pip install scapy

from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

if __name__ == "__main__":
    try:
        print("Capturing packets... (Ctrl+C to stop)")
        sniff(prn=packet_callback, store=False)  # store=Falseでメモリ節約
    except KeyboardInterrupt:
        print("\nCapture stopped.")
=======
#pip install scapy

from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

if __name__ == "__main__":
    try:
        print("Capturing packets... (Ctrl+C to stop)")
        sniff(prn=packet_callback, store=False)  # store=Falseでメモリ節約
    except KeyboardInterrupt:
        print("\nCapture stopped.")
>>>>>>> 5b35e2acb6c822b159da4f4255f6e59dca6d2b62
