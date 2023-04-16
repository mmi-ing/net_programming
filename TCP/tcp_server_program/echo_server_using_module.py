import MyTCPServer as my

port = 2500
BUFFSIZE = 1024

sock = my.TCPServer(port)
conn, addr = sock.Accept()
print('connected by', addr)

while True:
    data = conn.recv(BUFFSIZE)
    if not data:
        break
    print("Received message: ", data.decode())
    conn.send(data)

conn.close()