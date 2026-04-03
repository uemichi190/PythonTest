# HEAD
import pyshark
# 例: Windowsの場合
tshark_custom_path = r'C:\Program Files\Wireshark\tshark.exe'
# 例: Linux/macOSの場合 (もし /usr/local/bin にあれば)
# tshark_custom_path = '/usr/local/bin/tshark'
# FileCaptureの場合
#cap = pyshark.FileCapture('path/to/your/capture.pcap', tshark_path=tshark_custom_path)
cap = pyshark.FileCapture('sample.pcap', tshark_path=tshark_custom_path)
print(cap[0])
# LiveCaptureの場合
capcap = pyshark.LiveCapture(interface='eth0', tshark_path=tshark_custom_path)
print(capcap[0])
#
import pyshark
# 例: Windowsの場合
tshark_custom_path = r'C:\Program Files\Wireshark\tshark.exe'
# 例: Linux/macOSの場合 (もし /usr/local/bin にあれば)
# tshark_custom_path = '/usr/local/bin/tshark'
# FileCaptureの場合
#cap = pyshark.FileCapture('path/to/your/capture.pcap', tshark_path=tshark_custom_path)
cap = pyshark.FileCapture('sample.pcap', tshark_path=tshark_custom_path)
print(cap[0])
# LiveCaptureの場合
capcap = pyshark.LiveCapture(interface='eth0', tshark_path=tshark_custom_path)
print(capcap[0])
#s 5b35e2acb6c822b159da4f4255f6e59dca6d2b62
