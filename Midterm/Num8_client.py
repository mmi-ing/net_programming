from socket import *

port = 2500
BUFFSIZE = 1024

c_sock = socket(AF_INET, SOCK_DGRAM)

for i in range(4):    #4번 전송
    time = 2    #2초
    attemps = 0
    while True:
        msg = input('Enter the message("send mboxId message" or "receive mboxId"): ')
        if msg == 'quit':
            c_sock.sendto(msg.encode(), ('localhost', port))
            break
        c_sock.sendto(msg.encode(), ('localhost', port))
        c_sock.settimeout(time)
        try:
            data, addr = c_sock.recvfrom(BUFFSIZE)
        except timeout:
            time *= 1   #대기시간 증가 X
            attemps += 1
            if attemps > 3: #3회 시도
                break

        else:
            print(data.decode())

c_sock.close()
