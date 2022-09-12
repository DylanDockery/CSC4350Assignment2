# CSC4350Assignment2

Client/server application with 3 custom methods implemented.

Methods:
IP - Returns the IP address from the client request. Requires no parameters.
PORT - Returns the Port from the client request. Requires no parameters.
TIMEDELAY - Receive the date/time from the client. Calculates the time difference is seconds between what was received from the client and the current time. Returns the delay as well as the server's current date & time.

Server operation:
Start via commandline.
Commandline parameters are as follows:
-t --- Communication protocol that can be set to either TCP or UDP. Default is TCP.
-p --- Port used for server. Default is 8000

Client operation:
Start via commandline.
Commandline parameters are as follows:
-t --- Communication protocol that can be set to either TCP or UDP. Default is TCP.
-p --- Port for server. Default is 8000.
-i --- IP address for server Default is 127.0.0.1

Potential Improvements:
Time out on client if server is not active rather than having to use the keyboard interrupt
