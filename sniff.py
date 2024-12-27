from scapy.all import *
sniff(filter="src port 67",prn=lambda x: ls(x))
