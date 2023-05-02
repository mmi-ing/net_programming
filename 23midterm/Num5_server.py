from socket import *
from random import randint

s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 8888))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('connected by', addr)
    
    while True:
        data = conn.recv(1024).decode()
        last = 0
        last_value = last.to_bytes(4,'big')

        if not data:
            conn.sendall(f'0'.encode())
            break
        
        # 온도
        elif data == '1':
            temp = randint(1, 50)
            temp_value = temp.to_bytes(4, 'big')
            conn.sendall(f'Temp={temp_value}, Humid={last_value}, Lumi={last_value}'.encode())
       
       #습도
        elif data == '2':
            humid = randint(1, 100)
            humid_value = humid.to_bytes(4, 'big')
            conn.sendall(f'Temp={last_value}, Humid={humid_value}, Lumi={last_value}'.encode())
        
        #조도
        elif data == '3':
            Lumi = randint(1, 150)
            Lumi_value = Lumi.to_bytes(4, 'big')
            conn.sendall(f'Temp={last_value}, Humid={last_value}, Lumi={Lumi_value}'.encode())

    conn.close()