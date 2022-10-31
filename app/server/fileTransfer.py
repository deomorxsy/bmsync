#!/usr/bin/python3

import socket
import subprocess #substitute of os package

def fileTransfer(sock, host, port):
    try:
        ftSock = connect((host, port))
        #total = 0

        menuOption = input('/// Options\n
                    1- List files in shared directory
                    2- Upload a file
                    3- Download file
                    4- Synchronize files
                            ')
        if menuOption == 1:
            allFiles = os.listdir()
        elif menuOption == 2:
            upFilePath = '{}'.input('/// enter file path: ')
        elif menuOption == 3:

            downFileOpt = ''
        elif menuOption == 4:
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



if __name__ == '__main__':
    main()

