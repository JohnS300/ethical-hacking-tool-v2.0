import os
import sys
from scapy.all import ARP, Ether, srp

def scan_network(network_range):
    if os.geteuid() != 0:
        print("[+] This script must be run as root. Please call command with sudo.")
        sys.exit()

    arp = ARP(pdst=network_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=2, verbose=False)[0]

    devices = []
    for sent, received in result:
        devices.append((received.psrc, received.hwsrc))
        print(f"[+] Device IP: {received.psrc}, MAC: {received.hwsrc}")
    
    return devices
