from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))

while True:
    msg = input('Say Hello: ')
    s.sendall(msg.encode())

    data = s.recv(1024).decode()
    print(data)

    s.close()
