from socket import *

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('-> ')
    reTx = 0
    while reTx < 5: #재전송 횟수 5번 이하로 설정
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), ('localhost', port))
        sock.settimeout(2)

        try:
            data, addr = sock.recvfrom(BUFFSIZE)
            print('<- ', data.decode())
            break
        except timeout:
            reTx += 1   #timeout발생, 재전송 횟수 1증가
            continue
    else:
        break


sock.close()