#!/usr/bin/python3

from fileTransfer import *
from replication import *

from pathlib import Path
from socket import *
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

    serverMSG = "/// > Greetings, UDP client!"
    sendBytes = str.encode(serverMSG)
    dnsTable = {} #DNS table

    # Checks if DNS table exists with os-agnostic libpath library
    if (Path('../../var/dnsTable.json').exists()) == False:
        with open('../../var/dnsTable.json', 'w+') as f:
            f.write('')
            f.close()


    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        #_ = {executor.submit(load_url, url, 60) for connection in serverSocket }
        with socket(AF_INET, SOCK_DGRAM) as udpServerSock:
            udpServerSock.bind((suseIP, susePort))
            #serverSock.listen(10)

            # UDP connection does not requires an accept().
            # in case of a TCP connection, it does 3-way handshake.
            print('//// > Listening for incoming DATAGRAMS on 127.0.0.1:8080...')
            while True:
                #conn, addr = udpServerSock.accept() #UDP NAO INICIA CONEXAO
                #print("//// > IPV4 Connection established with address {}".format(addr))

                bytesAddressPair = udpServerSock.recv(bufferSize) # 1024 default for UDP. 2048 when using TCP
                clientMessage = bytesAddressPair[0] # retrieve message
                clientAddress = bytesAddressPair[1] # retrieve address

                foo = {} #holds dict

                with open('../var/dnsTable.json', 'r', ) as f:
                        clients = f.load(j)
                        for i in clients:
                            if '{}'.format(clientAddress) in dnsTable:
                                f.close()
                            elif not('{}'.format(clientAddress) in dnsTable):
                                dnsTable['{}'.format(clientAddress)] = socket.gethostbyaddr(clientAddress)
                                foo['{}'.format(clientAddress)] = socket.gethostbyaddr(clientAddress)
                                f.close()
                            else:
                                print('outra coisa')


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
                udpServerSock.sendto(sendBytes, address)

        # stablishes tcp connection
        with  socket(AF_INET, SOCK_STREAM) as tcpServerSock:
            fileTransfer(tcpServerSock, suseIP, 5005 )


                #print(type)
                #conn.close()
                #break
            #print(type(data))
            #print(data)


if __name__ == '__main__':
    main()

