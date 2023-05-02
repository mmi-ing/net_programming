from socket import *
import threading

PORT = 4567
BUF_SIZE = 1024

def recv_task(sock):
    while True:
        data = sock.recv(BUF_SIZE)
        print(data.decode())

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', PORT))

id = input('ID 를 입력하세요! : ')
sock.send(f'[{id}]'.encode())

th = threading.Thread(target=recv_task, args=(sock,))
th.daemon = True
th.start()

while True:
    msg = f'[{id}] ' + input()
    sock.send(msg.encode())