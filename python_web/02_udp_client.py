#import socket
#udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

from socket import*

udp_socket = socket(AF_INET, SOCK_DGRAM)
send_addr = ('10.123.164.100', 8080)

send_data = input("Please input the data you want to send:")
udp_socket.sendto(send_data.encode(encoding='utf-8'), send_addr)

recv_data = udp_socket.recvfrom(1024)
print(recv_data[0])
udp_socket.close()

