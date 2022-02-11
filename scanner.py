#!/bin/python3

import sys
import socket
from datetime import datetime

#endgame command --> python3 scanner.py <IP>

#Define target
if len(sys.argv) == 2: 
	target = socket.gethostbyname(sys.argv[1])  #target=2nd arg in endgame command; Translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <IP>")
	
	
#Adding a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)


try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator; #if port is open - 0; if closed - 1
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit() #ends program execution when Ctrl+C or Ctrl+Z is hit on keyboard
	

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
	
except socket.error:
	print("Could not connect to server.")
	sys.exit()
		
		
