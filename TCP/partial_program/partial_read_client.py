from socket import *

#create_connection() -> socket(), connect() 합쳐진 것
sock = create_connection(('localhost', 9999))

data_size = 20
rx_size = 0
total_data = []

while rx_size < data_size:
    #최대 4바이트 수신하도록 설정
    data = sock.recv(4)
    if not data:
        break
    rx_size += len(data)
    total_data.append(data.decode())
    print(total_data)

#20바이트보다 적어도 출력 가능
message = ''.join(total_data)
print(message)
sock.close()