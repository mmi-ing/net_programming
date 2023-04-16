from socket import *
import random

BUFFSIZE = 1024
port = 2500

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('localhost', port))

while True:
    msg, addr = s_sock.recvfrom(BUFFSIZE)
    if random.randint(1, 10) <= 4: #40% 데이터 손실
        print('Packet from {} lost!'.format(addr))
        continue
    print('Received: ', msg.decode())
    
    s_sock.sendto('ack'.encode(), addr)