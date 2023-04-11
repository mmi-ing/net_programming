from socket import *
from random import randint

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9000))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('Device 1 is connected by', addr)
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        if data == 'Request':
            # 데이터 생성
            temp = randint(0, 40)
            humid = randint(0, 100)
            illum = randint(70, 150)
            
            # 데이터 전송
            conn.sendall(f'Device 1: Temp={temp}, Humid={humid}, Illum={illum}'.encode())
        elif data == 'quit':
            print('Quit')
            conn.close()
            break
    
    conn.close()