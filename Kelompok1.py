# Kelompok 1

import psutil as ps
import time
import sys
import os
import subprocess

def get_monitoring(arg):
    ip = getip_by_iface(arg);

    print('\n')
    print('IP Address : '+ip)

    cpu = ps.cpu.percent()
    ram = ps.virtual_memory().percent
    print('CPU Used : {}\nRAM Used : {}'.format(cpu,ram))
    rx_bytes, tx_bytes = get_txrx(arg)
    rx_kb = int(rx_bytes)/1000
    tx_kb = int(tx_bytes)/1000
    print(f"Tx / Rx [eth] : {tx_kb}kbps / {rx_kb}kbps")
    time.sleep(2)

def get_txrx(interface):
    for line in open('/proc/net/dev', 'r'):
        if interface in line:
            data = line.split('%s:' % interface)[1].split()
            rx_bytes, tx_bytes = (data[0], data[8])
            return (rx_bytes, tx_bytes)

def getip_by_iface(iface):
    return os.popen("ip addr | grep "+iface+"| awk '{print $2}' | tail -n +2").read().strip();

def getallinterface():
    return subprocess.check_output("nmcli d | awk '{print $1}' | tail -n + 2 | head -n -1", shell = True, umiversal_newlines = True);

if __name__ == "__main__":
    os.system("clear")
    print("Pilih Mode : ")
    ifaces = getallinterface().split('\n')
    ifaces.remove("")
    for idx, iface in enumerate(iface):
        if (iface != ''):
            print("{0}. Mode {0}".format(idx+1));

    print("\nMasukkan Pilihan Anda : ");
    opti = int(input());
    if (opti < 1) or (opti > len(iface)):
        print('perintah tidak diketahui')
    else :
        get_monitoring(iface[opti-1])
        sys.exit(1);