from socket import *

port = 2500
BUFFSIZE = 1024

c_sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter the message("send mboxId message" or "receive mboxId"): ')
    if msg == 'quit':
        c_sock.sendto(msg.encode(), ('localhost', port))
        break

    c_sock.sendto(msg.encode(), ('localhost', port))
    data, addr = c_sock.recvfrom(BUFFSIZE)
    print(data.decode())

c_sock.close()
