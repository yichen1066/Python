from socket import*

server_socket = socket(AF_INET, SOCK_DGRAM)
bind_addr = ('', 7888)
server_socket.bind(bind_addr)

num = 1
while True:

    recv_data, send_addr = server_socket.recvfrom(1024)
    print(recv_data)

    send_data = input()
    server_socket.sendto(send_data.encode(encoding='utf-8'), send_addr)

server_socket.close()