#!/usr/bin/python3

from fileTransfer import *
from replication import *

from pathlib import Path

import socket # Following PEP 8, import without wildcards
import time
import sys
import concurrent.futures # threadpool executor
import json
import ast


def dnsParser(hostname): #pass hostnameFunction here
	addr = socket.gethostbyaddr(socket.gethostname())[2][0]
	dnsKeyPair = {addr: f'{hostname}'}
	line = str(dnsKeyPair)
	foobar = ast.literal_eval(line)
	dnsTablePath = './teste.json'

	#Since it doesn't exist yet, I don't need to read its contents. Append (writeable at the EOF if exists) only.
	if (Path(dnsTablePath).exists()) == False:
		with open(dnsTablePath, 'a') as f:
			f.write(json.dumps(foobar))
			f.close()
	# Now it matters if the address is there as key-value or not. Append (writeable at the EOF if exists) and '+' for updating (writing/reading) unlocks readable IO needed by json.load() method.
	elif (Path(dnsTablePath).exists()) == True:
		with open(dnsTablePath, 'r+') as f:
			dnsJson = json.load(f)
			if (addr in dnsJson) == False:
				f.write(json.dumps(foobar))
				f.close()
			else:
				f.close()

def main():
    #superserver
    suseIP = '127.0.0.1'
    susePort = 8080 #has to be int
    suseSocket = (suseIP, susePort)
    suseHost = socket.gethostname()
    addr = socket.gethostbyaddr(suseHost)[2][0]
    bufferSize = 1024 #For UDP datagram

    serverMSG = "/// > Greetings, UDP client!"
    sendBytes = str.encode(serverMSG)
    dnsKeyPair = {addr: suseHost} #DNS table
    dnsTablePath = '../../var/dnsTable.json'

    # Checks if DNS table exists with os-agnostic libpath library

    print("existe? {}".format(Path(dnsTablePath).exists()))
    if (Path(dnsTablePath).exists()) == False:
        with open(dnsTablePath, 'a') as f:
            f.write('{}'.format(dnsKeyPair))# ''
            f.close()


    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        #_ = {executor.submit(load_url, url, 60) for connection in serverSocket }
        with socket.socket(AF_INET, SOCK_DGRAM) as udpServerSock:
            udpServerSock.bind(suseSocket)
            #serverSock.listen(10)

            # UDP connection does not requires an accept().
            # in case of a TCP connection, it does 3-way handshake.
            print('//// > Listening for incoming DATAGRAMS on 127.0.0.1:8080...')
            while True:
                #conn, addr = udpServerSock.accept() #UDP NAO INICIA CONEXAO
                #print("//// > IPV4 Connection established with address {}".format(addr))

                #recvfrom to udp, recv for tcp? Yep.
                bytesAddressPair = udpServerSock.recvfrom(bufferSize) # 1024 default for UDP. 2048 when using TCP
                clientMessage = bytesAddressPair[0] # retrieve message
                clientAddress = bytesAddressPair[1][0] # retrieve address

                foo = {} #holds dict

                #print(bytesAddressPair)
                #the format is (b'Hello UDP Server', ('127.0.0.1', 37161))
				#

                hostnameFunction = socket.gethostname()#socket.gethostname()

                dnsParser(hostnameFunction) ## hostname flag


                clientMSG = "/// > Client found. Message:{}".format(clientMessage)
                clientIP = "/// > Client IP Address: {}".format(clientAddress)

                print(clientMSG)
                print(clientIP)


                #now reply to client with file
				#syntax for sendto is AF_INET address as second attribute, which is address and port.
                udpServerSock.sendto(sendBytes, (clientAddress, 8080))

        # stablishes tcp connection
        #with  socket(AF_INET, SOCK_STREAM) as tcpServerSock:
            #fileTransfer(tcpServerSock, addr, 5005 )



if __name__ == '__main__':
    main()

