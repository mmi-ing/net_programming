from socket import *

#create_server() -> socket(), bind(), listen() 합쳐진 것
server = create_server(('', 9999))
conn, addr = server.accept()

conn.send(b'This is IoT world!!!')  #아마 20바이트
conn.close()