from socket import*

def main():
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    server_addr = ('10.123.164.100', 8000)
    tcp_socket.bind(server_addr)
    tcp_socket.listen(5)

    client_socket, client_addr = tcp_socket.accept()
    recv_data = client_socket.recv(1024)
    str1 = format_str(str(recv_data))
    print("recieve data:%s"%str1)

    send_data = 'thank you!'
    client_socket.send(send_data.encode(encoding='utf-8'))

    client_socket.close()
    tcp_socket.close()

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