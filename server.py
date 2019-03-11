
# JOSE MUNGUIA
# jose02703@gmail.com
#UDP SOCKETS 

import socket
	# We will need the following module to generate randomized lost packets 
import random

def Main():
		
		port = 12005

		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		serverSocket.bind(('127.0.0.1',port))


		print ("Server Started.")
		while True:
			# Generate random number in the range of 0 to 10
			rand = random.randint(0, 10)
			# Receive the client packet along with the address it is coming from
			data, addr = serverSocket.recvfrom(1024)
			
			print ("message From: " + str(addr))
			print ("from connected user: " + str(data))
			data = data.upper()
			print ("sending: " + str(data))
			
			# If rand is less is than 4, we consider the packet lost and do nothing 
			if rand < 4:
				
				continue
				
			serverSocket.sendto(data, addr)
		
		

if __name__ == '__main__':
		Main()
		
