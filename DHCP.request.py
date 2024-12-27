from scapy.all import *
from scapy.layers.dhcp import *


def detect_dhcp(pkt):
    if DHCP in pkt:
        Ether_request = Ether(src=pkt[Ether].dst,dst =("ff:ff:ff:ff:ff:ff"))
        IP_request = IP(src="0.0.0.0",dst="255.255.255.255")
        UDP_request = UDP(sport=68,dport=67)
        BOOTP_request = BOOTP(chaddr=pkt[BOOTP].chaddr,xid=pkt[BOOTP].xid)
        DHCP_request = DHCP(options=[("message-type",'request'),("server_id",pkt[DHCP].options[1][1]),("requested_addr",pkt[BOOTP].yiaddr),"end"])
        Request = Ether_request/IP_request/UDP_request/BOOTP_request/DHCP_request
        sendp(Request,iface="以太网")
        print(pkt[BOOTP].yiaddr+"正在分配")


sniff(filter="src port 67", prn=detect_dhcp)



