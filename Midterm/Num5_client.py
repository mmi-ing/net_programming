from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))

while True:
    msg = input('Select information (1 or 2 or 3): ')
    # if device == 'quit':
    #     for port in [9000, 9001]:
    #         s = socket(AF_INET, SOCK_STREAM)
    #         s.connect(('localhost', port))
    #         s.sendall('quit'.encode())
    #         s.close()
    #     break
    # elif device not in ('1', '2'):
    #     print('Invalid input')
    #     continue
    
    if msg == '1':
        s.sendall('1'.encode())
        temp_data = s.recv(1024).decode()

        # temp_data = f"{data}"
        print(temp_data)
            
    elif msg == '2':
        s.sendall('2'.encode())
        humid_data = s.recv(1024).decode()
        # data_with_time = f"{data}"
        print(humid_data)

    elif msg == '3':
        s.sendall('3'.encode())
        Lumi_data = s.recv(1024).decode()
        # data_with_time = f"{data}"
        print(Lumi_data)

    s.close()
