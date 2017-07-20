from socket import*

def main():
    client_socket = socket(AF_INET, SOCK_STREAM)
    send_addr = ('10.123.164.100', 8000)
    client_socket.connect(send_addr)

    send_data = input("Please input the data you want to send:")

    client_socket.send(send_data.encode(encoding='utf-8'))

    recv_data = client_socket.recv(1024)
    print("recieve:%s"%recv_data)
    client_socket.close()

if __name__ == '__main__':
    main()