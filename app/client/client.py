from socket import *
import time
import sys

def main():
    SUSE_IP = '127.0.0.1'
    SUSE_PORT = '8080'
    sock = (SUSE_IP, SUSE_PORT)

    # IPV4 connection, UDP
    clientSock = socket(AF_INET, SOCK_DGRAM)

    recvMsg = None
    sendMsg = input('//// Connecting to 127.0.0.1:8080 . . .\n//// Type a message message:\n// >  ')
    print(type(send_msg))
    print(str.encode(send_msg))

    #while send_msg != '\x18': # ctrl+X? Ctrl+c?
        #print('//// > Press CTRL-C to stop.\n')
        #clientSock.sendto('sup'.encode(), sock)
        #time.sleep(0.5)
        #recv_msg, _
        #recv_msg, _ = clientSock.recvfrom(1024) # numero de bytes aceitos
        #print('//// > Server response:\n'.format(recv_msg.decode('utf-8')))
        #print('//// > Type:')
        #send_msg = input()




    udp_client_socket.close()




if __name__ == '__main__':
    main()
