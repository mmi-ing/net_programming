from socket import *

port = 2500
BUFFSIZE = 1024

mboxes = {}

s_sock = socket(AF_INET, SOCK_STREAM)
s_sock.bind(('localhost', port))
s_sock.listen(1)

print('Server started. Waiting for clients...')

while True:
    conn, addr = s_sock.accept()
    print('Connected by', addr)

    while True:
        data = conn.recv(BUFFSIZE)
        if not data:
            break

        msg = data.decode()
        print("Received: ", msg)

        tokens = msg.split()
        command = tokens[0]

        if command == 'send':
            mbox_id = tokens[1]
            message = ' '.join(tokens[2:])
            if mbox_id not in mboxes:
                mboxes[mbox_id] = []
            mboxes[mbox_id].append(message)
            conn.sendall('OK'.encode())
        elif command == 'receive':
            mbox_id = tokens[1]
            if mbox_id in mboxes and len(mboxes[mbox_id]) > 0:
                message = mboxes[mbox_id][0]
                del mboxes[mbox_id][0]
                conn.sendall(message.encode())
            else:
                conn.sendall('No message'.encode())
        elif command == 'quit':
            break

    conn.close()