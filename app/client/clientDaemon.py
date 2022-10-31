#!/usr/bin/python3

from socket import *

def main():
    daemonPort = 8084
    clientHost = gethostname()
    clientAddr = gethostbyname('{}'.format(clientHost))

    clientDaemon = socket(AF_INET, SOCK_STREAM)
    clientDaemon.bind((clientAddr, daemonPort)) #listening on port 8084
    clientDaemon.listen()

    while (True):

        # Replica-server to client-daemon connection and address
        (repConn, repAddr) = clientDaemon.accept()
        print('Accepting connection request from {}:{}'.format(repAddr[0], repAddr[1]))

        # Gets replica information if needed
        data = repConn.recv(1024)
        print(data.decode())

        response = '/// Daemon says: Message received. Starting new Server...'
        repConn.send(response.encode())



if __name__ == '__main__':
    main()
