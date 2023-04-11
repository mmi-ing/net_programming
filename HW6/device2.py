from socket import *
from random import randint

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9001))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('Device 2 is connected by', addr)
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        if data == 'Request':
            # 데이터 생성
            heartbeat = randint(40, 140)
            steps = randint(2000, 6000)
            cal = randint(1000, 4000)
            
            # 데이터 전송
            conn.sendall(f'Device 2: Heartbeat={heartbeat}, Steps={steps}, Cal={cal}'.encode())
        elif data == 'quit':
            print('Quit')
            conn.close()
            break
    
    conn.close()
    print('Device 2 is disconnected')
