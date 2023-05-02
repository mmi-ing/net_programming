from socket import *

port = 2500
BUFFSIZE = 1024

c_sock = socket(AF_INET, SOCK_DGRAM)

for i in range(3):
    time = 1.0 #1초 간격
    attempts = 0
    while True:
        c_sock.sendto('ack'.encode(), ('localhost', port))
        c_sock.settimeout(time)
        try:
            data, addr = c_sock.recvfrom(BUFFSIZE)
            if data.decode() == 'ack':
                break
        except timeout:
            attempts += 1
            if attempts > 3:    #최대 재전송 횟수 3회
                break
        else:
            print("No ack received")
            continue
    if data:
        print('Server says:', data.decode())

c_sock.close()