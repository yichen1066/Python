from socket import*
from multiprocessing import Process
import re

document_root = './html'
server_address = (IP, PORT) = '', 7788

class web_server:
    address_family = AF_INET
    socket_type = SOCK_STREAM
    request_queue_size = 5
    def __init__(self, server_address):
        self.server_socket = socket(self.address_family, self.socket_type)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server_socket.bind(server_address)
        self.server_socket.listen(self.request_queue_size)

    def forever_server(self):
        while True:
            self.client_socket, client_addr = self.server_socket.accept()
            new_client_process = Process(target=self.handle_client)
            new_client_process.start()
            self.client_socket.close()

    def handle_client(self):
        recv_data = self.client_socket.recv(2014)
        request_header_lines = recv_data.splitlines()

        for line in request_header_lines:
            print(line)
       # r'[^/]+(/[^ ]*)'
        http_response_method = request_header_lines[0]
        get_file_name = re.match(r'[^/]+(/[^ ]*)', str(http_response_method)).group(1)

        if get_file_name == '/':
            file_name = document_root + '/index.html'
        else:
            file_name = document_root + get_file_name

        print("file name ===========>> %s"%file_name)

        try:
            fo = open(file_name)
        except IOError:
            response_header_lines = 'HTTP/1.1 404 not found\r\n'
            request_header_lines += '\r\n'
            response_body = '====sorry, file not found===='
        else:
            response_header_lines = 'HTTP/1.1 200 OK\r\n'
            response_header_lines += '\r\n'
            response_body = fo.read()
            fo.close()
        finally:
            response = response_header_lines + response_body
            self.client_socket.send(response.encode(encoding='utf-8'))
            self.client_socket.close()
def print(self):

def make_server(server_addr):
    server = web_server(server_addr)
    return server

def main():
    httpd = make_server(server_address)
    print("Web Server: Serving HTTP  on port %d"%PORT)
    httpd.forever_server()

if __name__ == '__main__':
    main()