from scapy.all import *
import pyshark
import datetime
import threading
from tkinter import *
import tkinter.ttk as ttk

### Parameters ###
w_width = 900
ifList = []
btn_list = ['Start', 'Stop']
RawData = []



### interface_list: Listing usable I/F ###
def interface_list():
    for i in ifaces.data.keys():
        iface = ifaces.data[i]
        flg = int(iface.flags)
        if ((flg & 0x20) == 0) and len(iface.ip):	# 0x20: Disconnected
            ifList.append(iface)

### set_clk: Getting I/F name for selected I/F (index) ###
def set_clk(dg, idx):
    global IFidx
    IFidx = idx
    frm1.ifname['text'] = ifList[IFidx].name
    dg.destroy()
    return

### select_clk: Dialog Window for Selection of Network I/F ###
def select_clk(frm):
    dlg = Toplevel(frm)
    dlg.title('Select Network I/F')
    dlg.geometry('300x200')
    dlg.grab_set()

    radio = []
    name = []
    selectedIF = IntVar()
    selectedIF.set(0)
    for i in range(len(ifList)):
        radio.append(Radiobutton(dlg, variable=selectedIF, value=i))
        name.append(Label(dlg, text=ifList[i].name))
    [radio[i].grid(row=i, column=0) for i in range(len(ifList))]
    [name[i].grid(row=i, column=1) for i in range(len(ifList))]
    dummy = Label(dlg, text=' ')
    dummy.grid(row=len(ifList), column=0)
    set_btn = ttk.Button(dlg, text='Set', style='W.TButton', command=lambda:set_clk(dlg, selectedIF.get()))
    set_btn.grid(row=len(ifList)+1, column=1)

### ShowDetail: Detail of Packet ###
def ShowDetail(event):
    pos = frm2.prt.index(INSERT)
    line = int(pos.split('.')[0])
    #print(line)
    #print(RawData[line-1])
    frm3.prt.config(state='normal')
    frm3.prt.delete(0.0, END)
    out = '<< Packet Number ' + str(line) + ' >>' + '\n\n'
    frm3.prt.insert(END, out)
    # Removal of special escape sequence
    out = str(RawData[line-1]).replace('\x1b\x5b\x30\x6d', '')
    out = out.replace('\x1b\x5b\x31\x6d', '')
    out = out.replace('\x1b\x5b\x33\x32\x6d', '')
    out = out.replace('\x1b\x5b\x33\x33\x6d', '')
    frm3.prt.insert(END, out)
    frm3.prt.config(state='disabled')

### CaptureThread: Thread for capturing network packet ###
def CaptureThread():
    global doing
    global capture
    frm3.prt.config(state='normal')
    frm3.prt.delete(0.0, END)
    frm3.prt.config(state='disabled')
    frm2.prt.config(state='normal')
    frm2.prt.delete(0.0, END)
    i = 1
    for raw_packet in capture.sniff_continuously():
        RawData.append(raw_packet)
        try:	# IP
            out = str(i) + ' ' + str(raw_packet.sniff_time) + ' Src:' + raw_packet.ip.src \
                + ' Dst:' + raw_packet.ip.dst + ' Proto:' + raw_packet.ip.proto
        except:	# non IP -> Ether
            out = str(i) + ' ' + str(raw_packet.sniff_time) + ' Src:' + raw_packet.eth.src \
                + ' Dst:' + raw_packet.eth.dst + ' Proto:' + raw_packet.eth.type
        frm2.prt.insert(END, out + '\n')
        frm2.prt.see('end')
        i += 1
        if doing == 0:	# "Stop" clicked
            break
    frm2.prt.config(state='disabled')

### start_clk: Start of Capture ###
def start_clk():
    global doing
    global capture
    global IFidx
    if doing == 0:
        RawData.clear()
        doing = 1
        dt=datetime.datetime.now()
        file = str(dt.strftime('%Y%m%d_%H%M%S')) +'.pcap'
        print(ifList[IFidx].name,"でキャプチャ開始")
        print(file,"で、記録")
        capture = pyshark.LiveCapture(interface=ifList[IFidx].name, output_file=file) # Must be here.
        th_Monitor = threading.Thread(target=CaptureThread, daemon=True)	# Run Thread
        th_Monitor.start()
    else:
        doing = 0
    frm1.start_btn['text'] = btn_list[doing]

##### Main Program #####
root = Tk()
root.geometry('900x600')
root.title('Netowkr Packet Capture')

# Init
interface_list()
IFidx = 0
doing = 0

# Making Frame
frm1 = Frame(root, width=w_width)
frm1.iflabel = Label(frm1, text='Network I/F: ')
frm1.iflabel.grid(row=0, column=0)
frm1.ifname = Label(frm1, text=ifList[0].name)
frm1.ifname.grid(row=0, column=1)
frm1.dummy1 = Label(frm1, text='\t\t')
frm1.dummy1.grid(row=0, column=2)
frm1.select_btn = ttk.Button(frm1, text='Select', style='W.TButton', command=lambda:select_clk(frm1))
frm1.select_btn.grid(row=0, column=3)
frm1.dummy2 = Label(frm1, text='\t')
frm1.dummy2.grid(row=0, column=4)
frm1.start_btn = ttk.Button(frm1, text=btn_list[doing], style='W.TButton', command=lambda:start_clk())
frm1.start_btn.grid(row=0, column=5)

frm2 = Frame(root, width=w_width)
frm2.prt = Text(frm2, font=("Courier New", 12), width=130, height=15)
frm2.ysc = Scrollbar(frm2, orient=VERTICAL, command=frm2.prt.yview)
frm2.ysc.pack(side=RIGHT, fill="y")
frm2.prt["yscrollcommand"] = frm2.ysc.set
frm2.prt.config(state='disabled')
frm2.prt.pack()
frm2.prt.bindtags(('Text','post-class-bindings', '.', 'all'))
frm2.prt.bind_class("post-class-bindings", "<Button-1>", ShowDetail)

frm3 = Frame(root, width=w_width)
frm3.prt = Text(frm3, font=("Courier New", 12), width=130, height=20, wrap=NONE) # for Horizontal Scroll
frm3.ysc = Scrollbar(frm3, orient=VERTICAL, command=frm3.prt.yview)
frm3.ysc.pack(side=RIGHT, fill="y")
frm3.prt["yscrollcommand"] = frm3.ysc.set
frm3.ysc2 = Scrollbar(frm3, orient=HORIZONTAL, command=frm3.prt.xview)
frm3.ysc2.pack(side=BOTTOM, fill="x")
frm3.prt["xscrollcommand"] = frm3.ysc2.set
frm3.prt.config(state='disabled')
frm3.prt.pack()

frm1.pack()
frm2.pack()
frm3.pack()

# Loop
root.mainloop()
