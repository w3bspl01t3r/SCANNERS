#!/usr/bin/python
import socket
import sys
from datetime import datetime
import subprocess
host=raw_input("[+] Please enter the host name to scan:")
host1=socket.gethostbyname(host)
host_name=socket.gethostname();
print ("hostname is ",host1)
print "-"*60
print "PLEASE WAIT!!!SCANNING THE REMOTE HOST"
print "-"*60
t1=datetime.now()
try:
	for port in range(1,1024):								##########DEFINE THE RANGE ACC. TO YOUR NEED############
		sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result=sock.connect_ex((host1,port))
		if result==0:
			print("Port %d is open" %(port))
except KeyboardInterrupt:
	print("You pressed ctrl+c.")
	sys.exit()

except socket.gaierror:
	print("Unknown host")
	sys.exit()
except socket.error:
	print("Host is unreachable")
	sys.exit()
t2=datetime.now()
total=t2-t1;
print("TOTAL SCANNING TIME IS ", total)

	
