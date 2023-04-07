from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    path = req[0].split()[1]
    
    if path == '/index.html':
        f = open('index.html', 'r', encoding='utf-8')
        mimeType = 'text/html'
    elif path == '/iot.png':
        f = open('iot.png', 'rb')
        mimeType = 'image/png'
    elif path == '/favicon.ico':
        f = open('favicon.ico', 'rb')
        mimeType = 'image/x-icon'
    else:
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<html><head><title>Not Found</title></head><body>Not Found</body></html>')
        c.close()
        continue

    data = f.read()

    c.send(b'HTTP/1.1 200 OK\r\n')
    c.send(('Content-Type: ' + mimeType + '\r\n').encode())
    c.send(b'\r\n')
    if mimeType == 'text/html':
        c.send(data.encode('euc-kr'))
    else:
        c.sendall(data)

    f.close()
    c.close()