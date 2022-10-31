#!/usr/bin/python3

from socket import *
import json

def replication():

    daemonPort = 8084

    with open('../var/dnsTable.json', 'r') as f:
        clients = f.load(f)
        randomAddr = random.sample(sorted(clients), 1)
        hostAddr = clients['randomAddr']
        f.close()

    #Create TCP/IP socket
    repSock = socket(AF_INET, SOCK_STREAM)

    #Connect socket to the same port as daemon (client daemon on port 8084)
    repSock.connect((hostAddr, daemonPort))

    # Send message to daemon listening
    serverSend = '/// > Server says on {}: Spawn new server'.format(daemonPort)
    repSock.send(serverSend.encode())
    print(serverSend)

    # Receive message if succeded
    daemonRecv = repSock.recv(1024)
    print('Daemon says on {}: {}'.format(daemonPort, daemonRecv.decode()))



if __name__ == '__main__':
    replication()
