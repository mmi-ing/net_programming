from socket import *

port = 2500
BUFFSIZE = 1024

c_sock = socket(AF_INET, SOCK_STREAM)
c_sock.connect(('localhost', port))

while True:
    msg = input('Enter the message("send mboxID message" or "receive mboxID"): ')
    if msg == 'quit':
        c_sock.sendall(msg.encode())
        break

    c_sock.sendall(msg.encode())
    data = c_sock.recv(BUFFSIZE)
    print(data.decode())

c_sock.close()