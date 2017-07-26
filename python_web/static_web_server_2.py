from socket import *
from multiprocessing import Process
import re

def handle_client(clientSocket):
    recv_data = clientSocket.recv(2014)
    request_header_lines = recv_data.splitlines()

    for line in request_header_lines:
        print(line)
    http_response_method = request_header_lines[0]
    file_name = re.match(r'[^/]+(/[^ ]*)', str(http_response_method)).group(1)
    print("file name:%s"%file_name)

    if file_name == '/':
        file_name = document_root + '/index.html'
    else:
        file_name = document_root + file_name
    print("file name is ====2>%s"%file_name)

    try:
        f = open(file_name)
    except IOError:
        response_header_line = 'HTTP/1.1 404 not found\r\n'
        request_header_lines += '\r\n'
        response_body = '=====Sorry, file not found====='
    else:
        response_header_line = 'HTTP/1.1 200 OK\r\n'
        response_header_line += '\r\n'
        response_body = f.read()
        f.close()
    finally:
        response = response_header_line + response_body
        clientSocket.send(response.encode(encoding='utf-8'))
        clientSocket.close()

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind(('', 7799))
    serverSocket.listen(10)

    while True:
        clientSocket, clientAddr = serverSocket.accept()
        process = Process(target=handle_client, args=(clientSocket,))
        process.start()
        clientSocket.close()

document_root = './html'

if __name__ == '__main__':
    main()