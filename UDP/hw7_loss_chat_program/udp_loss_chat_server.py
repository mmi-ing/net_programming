from socket import *
import random
import time

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('localhost', port))

while True:
    sock.settimeout(None)
    reTx = 0
    while reTx < 5:
        data, addr = sock.recvfrom(BUFFSIZE)
        resp = str(reTx) + ' ' + data.decode()
        if random.random() <= 0.5: #50% 확률로 응답하지 않음
            continue
        else:
            print('<-', data.decode())
            resp = input('-> ')
            resp = str(reTx) + ' ' + resp
            sock.sendto(resp.encode(), addr)
            break