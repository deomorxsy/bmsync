#!/usr/bin/python3

import socket
import subprocess #substitute of os package

def fileTransfer(sock, host, port):
    try:
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
                    self.sock.send(l)
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

        '''
        if (Path('../var/dnsTable.json').exists()) == False:
            with open('../var/dnsTable.json', 'w+') as f:
                f.write('')
                f.close()
        elif:
            pass

        while total < MSGLEN:
            sent = ftSock.send('../var/dnsTable.json')
            print('Sending {}......'.format(sent))
            if sent == 0:
                raise RuntimeError("Socket connection broken OR data source is 0")
            totalSent = total + sent
        ftSocket.close()
        '''



#if __name__ == '__main__':
#    main()

