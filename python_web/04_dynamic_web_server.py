from socket import*
from multiprocessing import Process
import re
import sys

DOCUMENT_ROOT_DIR = './html'
SERVER_ADDRESS = (IP, PORT) = '', 7789
CTIME_ROOT_DIR = "./WSGIPython"

class web_server:
    address_family = AF_INET
    socket_type = SOCK_STREAM
    request_queue_size = 5

    # create sokcet
    def __init__(self, server_address):
        self.server_socket = socket(self.address_family, self.socket_type)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server_socket.bind(server_address)
        self.server_socket.listen(self.request_queue_size)

    # use multiprocessing model to deal with client socket request
    def forever_server(self):
        while True:
            self.client_socket, client_addr = self.server_socket.accept()
            new_client_process = Process(target=self.handle_client)
            new_client_process.start()
            self.client_socket.close()

    def start_response(self, status, headers):
        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers += "%s: %s\r\n"%header

        self.response_headers = response_headers
        print("response headers:")
        print(response_headers)

    def handle_client(self):
        recv_data = self.client_socket.recv(2014)
        request_header_lines = recv_data.splitlines()

        for line in request_header_lines:
            print(line)
        http_response_method = request_header_lines[0]
        method = re.match(r'(\w+) /[^ ]*', http_response_method.decode('utf-8')).group(1)
        get_file_name = re.match(r'\w+ (/[^ ]*)', http_response_method.decode('utf-8')).group(1)

        # decide whether the request is to execute a python script file or not
        if get_file_name.endswith('.py'):
            try:
                m = __import__(get_file_name[1:-3])
            except Exception:
                self.response_headers = 'HTTP/1.1 404 Not Found\r\n'
                response_body = 'File Not Found'
            else:
                env = {
                    'Path Info': get_file_name,
                    'Method': method
                }
                response_body = m.application(env, self.start_response)

            response = self.response_headers + "\r\n" + response_body
        else:
            if get_file_name == '/':
                file_name = DOCUMENT_ROOT_DIR + '/index.html'
            else:
                file_name = DOCUMENT_ROOT_DIR + get_file_name

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

def make_server(server_addr):
    server = web_server(server_addr)
    return server

def main():
    sys.path.insert(1, CTIME_ROOT_DIR)
    httpd = make_server(SERVER_ADDRESS)

    print("Web Server: Serving HTTP  on port %d"%PORT)
    httpd.forever_server()

if __name__ == '__main__':
    main()