import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

while True:
    try:
        expression = input()
        if expression.strip() == 'q':  # 공백을 제거한 뒤 비교
            sock.send(b'q')
            break
        else:
            sock.send(expression.encode())  #서버로 전송
            result_bytes = sock.recv(1024)  #서버에서 결과값을 받음
            print(result_bytes.decode())    #출력
    except:
        print('connection closed')
        break

sock.close()
