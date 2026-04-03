#pip install pyshark
#pip install codecs

import pyshark
import codecs
import time
import asyncio

#前処理
print("前処理")
#loop = asyncio.get_event_loop()
#loop.run_until_complete(do_task())

#関数定義
def main():
    func_a()
    #func_b()

def func_a():
    #cap = pyshark.FileCapture('C:/Users/user/sample.pcap')
    cap = pyshark.FileCapture('sample.pcap')
    print(cap[0])  # 最初のパケットを表示
    func_c(cap)
    cap.close()

def func_b():
    cap = pyshark.LiveCapture(interface = 'Wi-Fi')
    cap.sniff(timeout=10)
    func_c(cap)
    cap.close()

def func_c():
    packet = cap[0]
    print(packet.highest_layer)  # 例: HTTP
    print(packet.ip.src)         # 送信元IP
    print(packet.tcp.dstport)    # 宛先ポート

def do_subtask_1():
    print("do_subtask_1")

def do_subtask_2():
    print("do_subtask_1")
    
async def do_task():
    yield do_subtask_1()
    yield asyncio.sleep(1)
    yield do_subtask_2()


#メイン処理
if __name__ == "__main__":
    

    print("起動")
    #main();
   
    #cap = pyshark.FileCapture('C:/Users/user/sample.pcap')
    cap = pyshark.FileCapture('sample.pcap')
    print(cap[0])  # 最初のパケットを表示
    func_c(cap)
    cap.close()

