#!/usr/bin/python3

import os
import errno
import socket
import subprocess #substitute of os package

def fileTransfer(sock, host, port):
    ftSock = connect((host, port))
    #total = 0

    menuOption = input('/// Options\n1- List files in shared directory\n2- Upload a file\n3- Download file\n4- Synchronize files')
    if menuOption == 1:
        allFiles = os.listdir()
    elif menuOption == 2:
        filename = '{}'.input('/// enter file path: ')
        #upload = send(upFilePath, os.path.getsize(upFilePath))
        #filename = 'anon234.jpeg'
        f = open(filename, 'rb')
        while True:
            l = f.read(1024)
            while (l):
                sock.send(l)
                l = f.read(1024)

            if not l:
                f.close()

    elif menuOption == 3:
        downFileOpt = ''
    elif menuOption == 4:
        downFileOpt == ''
    else:
        print('Nothing to do. Closing conection...')



    ftSock.send('')


if __name__ == '__main__':
    fileTransfer()

