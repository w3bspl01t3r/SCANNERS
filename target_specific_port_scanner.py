#!/usr/bin/python
import sys
from socket import *
import optparse
from threading import *
def connScan(tgthost,tgtport):
	try:
		sock=socket(AF_INET,SOCK_STREAM)
		sock.connect((tgthost,tgtport))
		print "[+]%d/tcp PORT IS OPEN" %tgtport
	except:
		print "[-]%d/tcp PORT IS CLOSED" % tgtport
def portscan(tgthost,tgtports):
	try:
		tgtip=gethostbyname(tgthost)
	except:
		print "HOST IS UN REACHABLE:"
		exit(0)
	try:
		tgtName=gethostbyaddr(tgtip)
		print "SCANNING RESULT FOR %s" %tgtName
	except:
		print "SCANNING RESULT FOR ",(tgtip)
	for i in  tgtports:
		t=Thread(target=connScan ,args=(tgthost,int(i)))
		t.start()
def main():
	parser=optparse.OptionParser("usage is " + "-H <taget host> -p <target port>")
	parser.add_option("-H", dest="tgthost", type="string" ,help="specify the target host")
	parser.add_option("-p", dest="tgtport", type="string" ,help="sepcify ports win comma")
	(options,args)=parser.parse_args()
	tgthost=options.tgthost
	tgtports=str(options.tgtport).split(",")
	if(tgthost == None) | (tgtports[0] == None):
		print parser.usage
		exit(0)
	portscan(tgthost,tgtports)
if __name__=="__main__":
	main()
