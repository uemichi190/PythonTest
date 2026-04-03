<<<<<<< HEAD
import pyshark

cap = pyshark.LiveCapture ('Wi-Fi', bpf_filter='tcp port 23')  
#for pkt in cap:
#    if 'TELNET' in pkt:
#        try:
#            out = pkt.telnet
#            if 'Username' in str(out):
#                print('ユーザー名:')
#            elif 'Password' in str(out):
#                print('パスワード:')
#
#            if pkt.telnet.data:
#                print(out)
#        except:
=======
import pyshark

cap = pyshark.LiveCapture ('Wi-Fi', bpf_filter='tcp port 23')  
#for pkt in cap:
#    if 'TELNET' in pkt:
#        try:
#            out = pkt.telnet
#            if 'Username' in str(out):
#                print('ユーザー名:')
#            elif 'Password' in str(out):
#                print('パスワード:')
#
#            if pkt.telnet.data:
#                print(out)
#        except:
>>>>>>> 5b35e2acb6c822b159da4f4255f6e59dca6d2b62
#            pass