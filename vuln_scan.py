#!/usr/bin/python
import socket
import os
import sys
from datetime import *
def vulnscan(banner,filename):
	file1=open(filename , "r")
	for i in file1.readlines():
		if i.strip() in banner:
			print"[+]SYSTEM IS VULNEARABLE:" + i.strip()
def retbanner(target_ip,target_port):
	try:
		sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.connect((target_ip,target_port))
		banner=sock.recv(1024)
		return banner
	except:
		return
def main():
	t1=datetime.now()
	if len(sys.argv)==2:
		filename=sys.argv[1]
		if not os.path.isfile(filename):
			print "[-]FILE DOESN'T EXIST"
			exit(0)
		if not os.access(filename,os.R_OK):
			print"[-]ACCES DENIED(THIS FILE DON'T HAVE READING PERMISSION"
			exit(0)
	else:
		print "[+]USAGE ./vulnscan.py <filename>"			#######HERE THE FIlE NAME IS THE LIST OF VULNERABILITY AVAILABLE###############
		exit(0)
	for port in range(20,26):
		for i in range (31,33):							#######DEFINE THE RANGE ACC TO YOUR IP RANGE################
			target_ip="192.168.137." + str(i)				#######DEFINE THE TARGET_IP STRING ACC. TO YOUR IP RANGE##########
			banner=retbanner(target_ip,port)
			if banner:
				vulnscan(banner,filename)
	t2=datetime.now()
	t3=t2-t1
	print "total time ", t3
if __name__=="__main__":
	main()
