
# JOSE MUNGUIA
# jose02703@gmail.com 
#UDP SOCKETS 


# libraries for sockets
import socket 
import sys
# libraries for date
from datetime import date
from datetime import datetime 
import time
# for stats
import numpy as np
import decimal, numpy

def Main():
	
	
	rttStats=[] # for stats
	udpLost=0
	
	for count in range(10):
			
		# ip address and port # where the client can be reached
			host='127.0.0.1'
			port= 2019
			
			
			#specify the server address and port
			# UPD does not remember connections. 
			server= ("127.0.0.1", 12005)
			
			# set up client socket
			clientSocket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			#where client can be reached
			clientSocket.bind((host, port))
		
		
			# set time out to 1sec
			clientSocket.settimeout(1.0)
			
			# send 10 pings to server
			message="ping";
			clientSocket.sendto(message, server)
			# start counting time as soon as we send the mesage
			startingTime = time.time()
			try:
				#message from server
				messageFromServer,Serveraddress= clientSocket.recvfrom(1024) 
				# calculate
				endTime=time.time()
				elapsedTime=endTime-startingTime
				#get: day, month, month-date, time, year
				now=datetime.now()
				today= now.strftime("%c")
				print 'Reply from:' , Serveraddress ,':',str(messageFromServer),count+1,today.upper()
				
				print 'RTT:', elapsedTime *1000, 'ms'
				# add RTT time to array for stats
				rttStats.append(elapsedTime)
				print("\n")
			except socket.timeout:
				print 'Request timed out'
				# UDP package was lost 
				udpLost=udpLost+1
	#close connection
	clientSocket.close() 
	max_value = max(rttStats)
	min_value = min(rttStats)
	avg_value = sum(rttStats)/len(rttStats)
	
	print '----RTT STATS-----'
	print 'Min:', min_value *1000, 'ms'
	print 'Max:', max_value *1000, 'ms'
	print 'Average:', avg_value *1000, 'ms'
	print 'Package Lost:', udpLost
	print 'UDP Package Lost:' ,100 * float(udpLost)/float(10),'%' 	
	
if __name__ == '__main__':
	Main()						



