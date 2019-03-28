from socket import *
import string
import time

### Creating a socket of basic type

s = socket(AF_INET, SOCK_STREAM)

### Define banner

sendData1 = "This is the Organization's SMTP MAIL Service, Login detected at" + time.strftime("%a, %d %b %Y %H:%M:%S %Z") 

### Query IP address and set PORT

HOST = '127.0.0.1'
PORT = 1234

s.bind((HOST, PORT))	#Bind the socket to an IP and PORT
s.listen(1)				#Listen for a connection
incoming_socket, address = s.accept()
print (sendData1)
straddress  = str(address)

testlist	= straddress.split(',')
gethost		= testlist[0].split("'")
getaddr		= testlist[1].split(')')

host = gethost[1]  		#Remove just the address from the list
incoming_port = int(getaddr[0])		# Remove just the port number from the address
sendData2 = "Illegal Access of this server, your IP [" + host +"] has been logged." 	# Define warning
print "Connection attempt on port", PORT, "from", host, ":", incoming_port 				# Print connection info 

data = incoming_socket.recv(1024)		# Listen for incoming data
incoming_socket.send(sendData2)
incoming_socket.close