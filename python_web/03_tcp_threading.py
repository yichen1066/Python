from socket import *
from threading import Thread

def recieve():
    while True:
        client_socket, client_addr = server_socket.accept()
        print("ip %s connected" % client_addr[0])
        recieve_data = client_socket.recv(1024)

        if len(recieve_data) == 3:
            return
        else:
            print("%s send message:%s"%(client_addr[0], format_str(str(recieve_data))))

def main():
    global server_socket
    global client_socket
    global client_addr
    server_socket = socket(AF_INET, SOCK_STREAM)
    addr = ('', 8000)
    server_socket.bind(addr)
    server_socket.listen(5)

    tr1 = Thread(target=recieve)
    tr1.run()
    tr1.join()

    server_socket.close()

def format_str(string):
    size = len(string)
    import re
    str = re.findall(r'[^b]', string)
    new_str = str[1:(len(str)-5)]
    s = ''
    for i in range(len(new_str)):
        s += new_str[i]
    return s

if __name__ == '__main__':
    main()