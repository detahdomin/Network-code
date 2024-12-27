from scapy.all import *
from scapy.layers.dhcp import *
import binascii
import random
random_MAC = str(RandMAC())
random_binMAC = binascii.unhexlify(random_MAC.replace(":",""))
xid_random = random.randint(0,1000000)
iface_=input("输入发送的网卡:")
def dhcp_discover(MAC,xid_,MAC_bin,iface_):
    Ether_discover=Ether(src=MAC, dst="ff:ff:ff:ff:ff:ff")

    IP_discover=IP(src="0.0.0.0", dst="255.255.255.255")

    UDP_discover=UDP(sport=68, dport=67)

    BOOTP_discover=BOOTP(chaddr=MAC_bin,xid=xid_)

    DHCP_discover=DHCP(options=[("message-type","discover"),"end"])

    discover=Ether_discover/IP_discover/UDP_discover/BOOTP_discover/DHCP_discover

    sendp(discover,iface=(iface_))

dhcp_discover(random_MAC,xid_random,random_binMAC,iface_)
print(f"随机的MAC地址为{random_MAC},16为MAC地址{random_binMAC},网卡为:{iface_}")



    