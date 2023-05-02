from socket import *
import random

port = 2500
BUFFSIZE = 1024

mboxes = {}

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('localhost', port))

while True:
    data, addr = s_sock.recvfrom(BUFFSIZE)
    msg = data.decode()
    print('Received:', msg)

    tokens = msg.split()
    command = tokens[0]

    if command == 'send':
        mbox_id = tokens[1]
        message = ' '.join(tokens[2:])
        if mbox_id not in mboxes:
            mboxes[mbox_id] = []
        mboxes[mbox_id].append(message)
        if random.random() <= 0.1: #10% 확률로 응답하지 않음
            continue
        else:
            s_sock.sendto('OK'.encode(), addr)
    elif command == 'receive':
        mbox_id = tokens[1]
        if random.random() <= 0.1: #10% 확률로 응답하지 않음
            continue
        elif mbox_id in mboxes and len(mboxes[mbox_id]) > 0:
            message = mboxes[mbox_id][0]
            del mboxes[mbox_id][0]
            s_sock.sendto(message.encode(), addr)
        else:
            s_sock.sendto('No messages'.encode(), addr)
    elif command == 'quit':
        break

s_sock.close()
