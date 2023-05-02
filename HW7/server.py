import socket
import threading
import time

clients = []
PORT = 4567
BUF_SIZE = 1024

def server_task(sock, addr):
    while True:
        data = sock.recv(BUF_SIZE)

        if 'quit' in data.decode() and sock in clients:
            print(addr, ': exited')
            clients.remove(sock)
            continue

        print(time.asctime() + str(addr) + ':' + data.decode())

        for x in clients:
            if x != sock:
                x.send(data)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(50)

print('=' * 20 + 'Server Started' + '=' * 20)

while True:
    conn, addr = s.accept()
    clients.append(conn)
    print(conn, ': connected')
    threading.Thread(target=server_task, args=(conn, addr)).start()