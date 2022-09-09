from socket import *
from datetime import datetime
import argparse
parser = argparse.ArgumentParser(description='Server')
parser.add_argument('-t', type=str, default='TCP', help='Communication protocol that can be set to either TCP or UDP. Default is TCP')
parser.add_argument('-p', type=int, default=8000,help='Port for server. Default is 8000')
parser.add_argument('-i', type=str, default='127.0.0.1',help='IP address for server Default is 127.0.0.1')
args = parser.parse_args()

if args.p != 8000:
    serverPort=args.p
else:
    serverPort=8000

if args.i != '127.0.0.1':
    serverName=args.i
else:
    serverName='127.0.0.1'

if(args.t !='TCP' and args.t!='UDP'):
        print('INVALID PROTOCOL DEFAULTED TO TCP')

selection = int(input('1- IP address\n2- Port\n3- Time Delay\n4- Quit (close the connection)\n'))
while selection!=4:
    if selection in (1,2,3):
        if selection == 1:
            message = 'IP'
        elif selection == 2:
            message = 'PORT'
        else:
            message = 'TIMEDELAY'+'_'+ str(datetime.now().timestamp())
        if args.t == 'UDP':
            clientSocket = socket(AF_INET,SOCK_DGRAM)
            clientSocket.sendto(message.encode(),(serverName,serverPort))
            modifiedMessage, serverAddress=clientSocket.recvfrom(2048)
            currentTime = datetime.now().timestamp()
            if selection != 3:
                print(modifiedMessage.decode())
            else:
                returnMessage=modifiedMessage.decode().split('_')
                returnTime=currentTime-float(returnMessage[2])
                print('Server date and time: '+returnMessage[0]+'\nTime from client to server: '+returnMessage[1]+'\nTime from client to server: '+str(returnTime))

            clientSocket.close()



        else:
            clientSocket = socket(AF_INET,SOCK_STREAM)
            clientSocket.connect((serverName,serverPort))
            clientSocket.send(message.encode())
            modifiedMessage, serverAddress=clientSocket.recvfrom(2048)
            currentTime = datetime.now().timestamp()
            if selection != 3:
                print(modifiedMessage.decode())
            else:
                returnMessage=modifiedMessage.decode().split('_')
                returnTime=currentTime-float(returnMessage[2])
                print('Server date and time: '+returnMessage[0]+'\nTime from client to server: '+returnMessage[1]+'\nTime from client to server: '+str(returnTime))

            clientSocket.close()
    
    selection = int(input('1- IP address\n2- Port\n3- Time Delay\n4- Quit (close the connection)\n'))
