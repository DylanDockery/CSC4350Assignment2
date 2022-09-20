#Dylan Dockery
#Server portion of client server spplication
#libraries needed : socket, argparse, datetime
#instructions: 
#Start via commandline. Commandline parameters are as follows: -t --- Communication protocol that can be set to either TCP or UDP. Default is TCP. 
#-p --- Port used for server. Default is 8000

from socket import *
import argparse
from datetime import datetime

#logs requests from clients in the form DATETIME REQUEST_METHOD RESPONSE_CODE in serverLog.txt
def logRequest(requestMethod,responseCode):
    f=open("serverLog.txt","a")
    f.write(str(datetime.now())+' '+requestMethod+' '+responseCode+'\n')
    f.close()

#determines response to client
def response(message,clientAddress):
    #variables for indices during string processing
    IPindex=0
    portIndex=1
    sentTimeIndex=1
    methodIndex=0

    okCode='OK'
    invalidCode='INVALID'
    requestMethod=message.split('_')[methodIndex]

    #IP method handling
    if requestMethod == 'IP':
        logRequest(requestMethod,okCode)
        returnMessage = okCode+'_' + clientAddress[IPindex]
    
    #PORT method handling
    elif requestMethod == 'PORT':
        logRequest(requestMethod,okCode)
        returnMessage = okCode+'_'+ str(clientAddress[portIndex])
        return returnMessage

    #TIMEDELAY method handling
    elif requestMethod == 'TIMEDELAY':
        #time from client and current time and returns invalid if date time not included
        try:
            messageSplit=message.split('_')
            time=datetime.now()
            time_sec=time.timestamp()
            senttime=float(messageSplit[sentTimeIndex])
            deltatime= time_sec - senttime
            logRequest(messageSplit[methodIndex],okCode)
            returnMessage = okCode+'_'+str(time)+'_'+str(deltatime)+'_'+str(time_sec)
            return returnMessage
        except:
            logRequest(requestMethod,invalidCode)
            returnMessage = invalidCode

    #Hand    
    else:
        logRequest(requestMethod,invalidCode)
        returnMessage = invalidCode
    return returnMessage

    
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
        returnMessage= response(message.decode(),clientAddress)
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
        returnMessage= response(message,addr)

        connectionSocket.send(returnMessage.encode())
        connectionSocket.close()
