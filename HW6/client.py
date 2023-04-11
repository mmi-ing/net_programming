from socket import *
import time

while True:
    device = input('Select Device (1 or 2): ')
    if device == 'quit':
        for port in [9000, 9001]:
            s = socket(AF_INET, SOCK_STREAM)
            s.connect(('localhost', port))
            s.sendall('quit'.encode())
            s.close()
        break
    elif device not in ('1', '2'):
        print('Invalid input')
        continue
    
    s = socket(AF_INET, SOCK_STREAM)
    if device == '1':
        s.connect(('localhost', 9000))
        s.sendall('Request'.encode())
        data = s.recv(1024).decode()
        cur_time = time.strftime('%a %b %d %H:%M:%S %Y')
        data_with_time = f"{cur_time}: {data}"
        print(data_with_time)
        
        with open('data.txt', 'a') as f:
            f.write(f"{data_with_time}\n")
            
    elif device == '2':
        s.connect(('localhost', 9001))
        s.sendall('Request'.encode())
        data = s.recv(1024).decode()
        cur_time = time.strftime('%a %b %d %H:%M:%S %Y')
        data_with_time = f"{cur_time}: {data}"
        print(data_with_time)
        
        with open('data.txt', 'a') as f:
            f.write(f"{data_with_time}\n")

    s.close()
