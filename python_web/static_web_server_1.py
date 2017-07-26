from socket import *
from multiprocessing import Process

def handleclient(clientSocket):
    recvData = clientSocket.recv(2014)
    requestHeaderlines = recvData.splitlines()

    for line in requestHeaderlines:
        print(line)
    responseHeaderlines = 'HTTP/1.1 200 OK\r\n'
    responseHeaderlines += '\r\n'
    responseBody = '包舒月是笨蛋'

    responseHeaderlines += responseBody
    clientSocket.send(responseHeaderlines.encode(encoding='gb2312'))

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind(('', 7788))
    serverSocket.listen(10)

    while True:
        clientSocket, clientAddr = serverSocket.accept()
        pro = Process(target=handleclient, args=(clientSocket,))
        pro.start()
        clientSocket.close()

if __name__ == '__main__':
    main()