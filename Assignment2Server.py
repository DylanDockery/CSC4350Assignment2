#Dylan Dockery
#Server portion of client server spplication
#libraries needed : socket, argparse, datetime
#instructions: 
#Start via commandline. Commandline parameters are as follows: -t --- Communication protocol that can be set to either TCP or UDP. Default is TCP. 
#-p --- Port used for server. Default is 8000

from socket import *
import argparse
from datetime import datetime

#command line argmuent declaration
parser = argparse.ArgumentParser(description='Server')
parser.add_argument('-t', type=str, default='TCP', help='Communication protocol that can be set to either TCP or UDP. Default is TCP')
parser.add_argument('-p', type=int, default=8000,help='Port used for server. Default is 8000')
args = parser.parse_args()

#set port
if args.p != 8000:
    serverPort=args.p
else:
    serverPort=8000
    
if(args.t not in ('TCP','UDP')):
    print('INVALID PROTOCOL DEFAULTED TO TCP')
    
    
#UDP handling 
if args.t == 'UDP':
    serverSocket = socket(AF_INET,SOCK_DGRAM)
    serverSocket.bind(('',serverPort))
    print("The server is ready to receive")
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        
        if message.decode() == 'IP':
            returnMessage = clientAddress[0]
        elif message.decode() == 'PORT':
            returnMessage = str(clientAddress[1])
        else:
            #time from client and current time 
            time=datetime.now()
            time_sec=time.timestamp()
            senttime=float(message.decode().split('_')[1])
            deltatime= time_sec - senttime
            
            returnMessage = str(time)+'_'+str(deltatime)+'_'+str(time_sec)

            

        serverSocket.sendto(returnMessage.encode(),clientAddress)
    


#TCP handling
else:
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print("The server is ready to receive")
    while True:
        
        connectionSocket, addr = serverSocket.accept()
        message = connectionSocket.recv(1024).decode()
        if message == 'IP':
            returnMessage = addr[0]
        elif message == 'PORT':
            returnMessage = str(addr[1])
        else:
            #time from client and current time
            time=datetime.now()
            time_sec=time.timestamp()
            senttime=float(message.split('_')[1])
            deltatime= time_sec - senttime
            
            returnMessage = str(time)+'_'+str(deltatime)+'_'+str(time_sec)

        connectionSocket.send(returnMessage.encode())
        connectionSocket.close()
