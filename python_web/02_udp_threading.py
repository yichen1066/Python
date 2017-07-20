from socket import*
from threading import Thread

def main():
    global udp_socket
    global dest_ip
    global dest_port

    dest_ip = input("ip:")
    dest_port = int(input("port:"))

    udp_socket = socket(AF_INET, SOCK_DGRAM)
    bind_addr = ('10.123.164.100', 8000)
    udp_socket.bind(bind_addr)
    recieve = Thread(target=accept)
    send_msg = Thread(target=send)

    recieve.start()
    send_msg.run()

    recieve.join()
    send_msg.join()
    udp_socket.close()

def accept():
    while True:
        accept_data, dest_addr = udp_socket.recvfrom(1024)
        print(format_str(str(accept_data)))

def send():
    while True:
        send_data = input("<<")
        dest_addr = (dest_ip, dest_port)
        udp_socket.sendto(send_data.encode(encoding='utf-8'), dest_addr)

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
