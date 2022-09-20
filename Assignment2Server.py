#Dylan Dockery
#Server portion of client server spplication
#libraries needed : socket, argparse, datetime
#instructions: 
#Start via commandline. Commandline parameters are as follows: -t --- Communication protocol that can be set to either TCP or UDP. Default is TCP. 
#-p --- Port used for server. Default is 8000

from socket import *
import argparse
from datetime import datetime

def logRequest(requestMethod,responseCode):
    f=open("serverLog.txt","a")
    f.write(str(datetime.now())+' '+requestMethod+' '+responseCode)
    f.close()

def response(message):
    requestMethod=message.decode()
    if requestMethod == 'IP':
        logRequest(requestMethod,'OK')
        return returnMessage = 'OK_' + clientAddress[0]
    elif requestMethod == 'PORT':
        logRequest(requestMethod,'OK')
        return returnMessage = 'OK_'+ str(clientAddress[1])
    elif requestMethod == 'TIMEDELAY':
        #time from client and current time 
        try:
            time=datetime.now()
            time_sec=time.timestamp()
            senttime=float(message.decode().split('_')[1])
            deltatime= time_sec - senttime
            logRequest(requestMethod,'OK')
            return returnMessage = 'OK_'+str(time)+'_'+str(deltatime)+'_'+str(time_sec)
        except:
            logRequest(requestMethod,'INVALID')
            return returnMessage = 'INVALID'
            
    else:
        logRequest(requestMethod,'INVALID')
        return returnMessage = 'INVALID'

    
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
        returnMesage= response(message)
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
        returnMesage= response(message)

        connectionSocket.send(returnMessage.encode())
        connectionSocket.close()
