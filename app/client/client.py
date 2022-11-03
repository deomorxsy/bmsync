import socket #pep 8, without wildcard * import.
import time
import sys

def main():
    #SUSE_IP = '127.0.0.1'
    #SUSE_PORT = '8080'
    #sock = (SUSE_IP, SUSE_PORT)

    # IPV4 connection, UDP
    #clientSock = socket(AF_INET, SOCK_DGRAM)

    #recvMsg = None
    #sendMsg = input('//// Connecting to 127.0.0.1:8080 . . .\n//// Type a message message:\n// >  ')
    #print(type(sendMsg))
    #print(str.encode(sendMsg))

    msgFromClient = "Hello UDP Server"
    bytesToSend = str.encode(msgFromClient)
    serverAddressPort = ("127.0.0.1", 8080)
    bufferSize = 1024

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from server {}".format(msgFromServer[0])
    print(msg)

    '''
    while sendMsg != '\x18': # ctrl+X? Ctrl+c?
        print('//// > Press CTRL-C to stop.\n')
        clientSock.sendto((str.encode("hello udp server")), sock) # encode()
        msgFromServer = UDPClientSocket.recvfrom(buffersize)
        #time.sleep(0.5)
        #recv_msg, _
        #recv_msg, _ = clientSock.recvfrom(1024) # numero de bytes aceitos
        #print('//// > Server response:\n'.format(recv_msg.decode('utf-8')))
        #print('//// > Type:')
        #sendMsg = input()
    '''




    clientSock.close()




if __name__ == '__main__':
    main()
