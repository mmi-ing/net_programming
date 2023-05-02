from socket import *
import random


port = 7777
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    if random.randint(1, 10) <= 4: #40% 데이터 손실
        print('Packet from {} lost!'.format(addr))
        continue
    if data.decode() == 'ping':
        sock.sendto('pong'.encode(), addr)