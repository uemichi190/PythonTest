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
#            pass