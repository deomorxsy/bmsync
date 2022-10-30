#!/usr/bin/python3

import pathlib
from socket import *
from fileTransfer import *
import time
import sys
import concurrent.futures # threadpool executor
import json

def main():
    suseIP = '127.0.0.1'
    susePort = 8080 #has to be int
    suseSocket = (suseIP, susePort)
    suseHost = gethostname()
    bufferSize = 1024 #For UDP datagram
    #serverSocket = socket(AF_INET, SOCK_DGRAM)
    #serverSocket.bind((gethostname(), 8080))
    #serverSocket.listen(5) # max 5 connections

    #SOCK_DGRAM = UDP, datagram socket with no connection
    #SOCK_STREAM = TCP,

    serverMSG = "/// > Greetings, UDP client!"
    sendBytes = str.encode(serverMSG)
    dnsTable = {} #DNS table

    # Checks if DNS table exists with os-agnostic libpath library
    if (Path('../var/dnsTable.json').exists()) == False:
        with open('../var/dnsTable.json', 'w+') as f:
            f.write('')
            f.close()


    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        #_ = {executor.submit(load_url, url, 60) for connection in serverSocket }
        with socket(AF_INET, SOCK_DGRAM) as serverSock:
            serverSock.bind((suseIP, susePort))
            #serverSock.listen(10)

            # UDP connection does not requires an accept().
            # in case of a TCP connection, it does 3-way handshake.
            print('//// > Listening for incoming DATAGRAMS on 127.0.0.1:8080...')
            while True:
                #conn, addr = serverSock.accept() #UDP NAO INICIA CONEXAO
                #print("//// > IPV4 Connection established with address {}".format(addr))

                bytesAddressPair = serverSock.recv(bufferSize) # 1024 default. Could also be 2048
                clientMessage = bytesAddressPair[0] # retrieve message
                clientAddress = bytesAddressPair[1] # retrieve address

                foo = {} #holds dict

                with open('../var/dnsTable.json', 'r', ) as f:
                        clients = f.load(j)
                        for i in clients:
                    if '{}'.format(clientAddress) in dnsTable:
                        f.close()
                    elif:
                        dnsTable['{}'.format(clientAddress)] = socket.gethostbyaddr(clientAddress))
                        foo['{}'.format(clientAddress)] = socket.gethostbyaddr(clientAddress)
                        f.close()


                if foo != 0:
                    j = json.dumps(foo)
                    with open('../var/dnsTable.json', 'a', ) as f:
                        f.write(j)
                        f.close()


                clientMSG = "/// > Client found. Message:{}".format(clientMessage)
                clientIP = "/// > Client IP Address: {}".format(clientAddress)

                print(clientMSG)
                print(clientIP)


                #now reply to client
                serverSock.sendto(sendBytes, address)

                # Reads Domain Name database and stablishes tcp connection
                fileTransfer()


                #print(type)
                #conn.close()
                #break
            #print(type(data))
            #print(data)


if __name__ == '__main__':
    main()

