#!/usr/bin/python
import socket
import os
import sys
from datetime import *
def vulnscan(banner,filename):
	file1=open(filename , "r")
	for i in file1.readlines():
		if i.decode('utf-8').strip() in banner:
			print("[+]SYSTEM IS VULNEARABLE:" + i.strip())
def retbanner(ip,port):
	try:
		sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		val=sock.connect((ip, port))
		if val!=-1:
			print("THE PORT IS OPEN===>" +ip+":"+str(port))
		if port==80:
			message = "HEAD / HTTP/1.1\r\n\r\n"
			sock.sendall(message)
			banner1=sock.recv(4096)
			ind=banner1.find('Server')
			ind=ind+7;
			banner=banner1[ind:83]
			return banner
		elif port==23:
			if val==-1:
				pass
			else:
				print("[+] TELNET DETECTED")
		else:
			banner=sock.recv(4096)
			return banner
	except socket.error as e:
		pass

def main():
	t1=datetime.now()
	if len(sys.argv)==2:
		filename=sys.argv[1]
		if not os.path.isfile(filename):
			print("[-]FILE DOESN'T EXIST")
			exit(0)
		if not os.access(filename,os.R_OK):
			print("[-]ACCES DENIED(THIS FILE DON'T HAVE READING PERMISSION")
			exit(0)
	else:
		print("[+]USAGE ./vulnscan.py <filename>")			#######HERE THE FIlE NAME IS THE LIST OF VULNERABILITY AVAILABLE###############
		exit(0)
	for port in range(20,24):
		for i in range (141,143):							#######DEFINE THE RANGE ACC TO YOUR IP RANGE################
			target_ip="10.5.241." + str(i)				#######DEFINE THE TARGET_IP STRING ACC. TO YOUR IP RANGE##########
			banner=retbanner(target_ip,port)
			if banner:
				vulnscan(banner,filename)
	t2=datetime.now()
	t3=t2-t1
	print("total time ", t3)
if __name__=="__main__":
	main()
