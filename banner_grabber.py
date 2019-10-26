#!/usr/bin/python
import socket
def retbanner(ip,port):
	try:
		sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.connect((ip,port))
		banner=sock.recv(2048)
		return banner
	except:
		exit(0)

def main():
	ip=raw_input("PLEASE ENTER THE IP:")
	port=int(raw_input("PLEASE ENTER THE PORT:"))
	banner=retbanner(ip,port)
	if banner:
		print "[+]"+ip+":"+str(port)+":"+banner
main()
