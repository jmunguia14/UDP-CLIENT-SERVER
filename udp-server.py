
# JOSE MUNGUIA
# jose02703@gmail.com
#UDP SOCKETS 


#A UDP client and server program for communication using Python sockets.
#The program can also be run in separate computer. Client has to know server's IP and port number in order to communicate. 
#Client will send 10 "ping" and the Server will return 10 "PING" capitalized. 
#In UDP is not a reliable protocol, so some packages may get lost. 
#Client waits one second for a packet, after that the client assumes that the package was lost. 
#At the end of the program, we get stats such as RTT(round trip time- the time for a message to go from client to server and back to client).
#Also, the average RTT for each message and other interesting stats.  




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
		
