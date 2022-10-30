from socket import *
import time
import sys

def main():
    SUSE_IP = '127.0.0.1'
    SUSE_PORT = '8080'
    SOCKET = (SUSE_IP, SUSE_PORT)

    # IPV4 connection, UDP
    client_sock = socket(AF_INET, SOCK_DGRAM)

    recv_msg = None
    send_msg = input('//// Connecting to 127.0.0.1:8080 . . .\n//// > Type a message message')

    while send_msg != '\x18': # ctrl+X? Ctrl+c?
        print('//// > Press CTRL-C to stop.\n')
        client_sock.sendto(send_msg.encode(), SOCKET)
        time.sleep(0.5)
        recv_msg, _ = client_sock.recvfrom(2048) # numero de bytes aceitos
        print('//// > Server response:\n'.format(recv_msg.decode('utf-8')))
        print('//// > Type:')
        send_msg = input()

    udp_client_socket.close()




if __name__ == '__main__':
    main()
