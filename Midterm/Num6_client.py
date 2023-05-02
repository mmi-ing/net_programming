from socket import *
import time

port = 7777
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

for i in 3 :    #3번 전송
    while True:
        msg = input('input ping: ')
        sock.sendto(msg.encode(), ('localhost', port))
        msg_time = time.time()
        attemp_time = 1.0 #1초 간격
        sock.settimeout(attemp_time)
        time_attempt = 0

        try :
            data, addr = sock.recvfrom(BUFFSIZE)
            if data.decode() == 'pong':
                msg_time_time = time.time()
                msg__time = msg_time_time - msg_time
            print('Success (RTT:{})'.format(msg__time))
        except timeout:
            time_attempt += 1 
            if time_attempt > 2:
                break
            print('Fail')
            
