from socket import *

relay_server = socket(AF_INET, SOCK_DGRAM)
relay_server.bind(('localhost', 9000))

while True:
    browser_data, browser_addr = relay_server.recvfrom(1024)

    # # 브라우저로부터 받은 HTTP 요청 메시지에서 호스트 이름 추출
    # host = None
    # for line in browser_data.split(b'\r\n'):
    #     if line.startswith(b'Host:'):
    #         host = line.split(b' ')[1].decode()
    #         break

    # # 호스트 이름이 추출되지 않았을 경우 연결 종료
    # if host is None:
    #     continue

    # 호스트 이름이 localhost인 경우, www.daum.net으로 변경
    if host == 'localhost':
        host = 'www.daum.net'

    # 브라우저로부터 받은 HTTP 요청 메시지를 외부 서버에 전송
    external_server = socket(AF_INET, SOCK_DGRAM)
    external_server.sendto(browser_data.replace(f'Host: localhost:9000'.encode(), f'Host: {host}'.encode()), (host, 80))

    # 외부 서버로부터 받은 HTTP 응답 메시지를 브라우저에게 전달
    while True:
        external_data, external_addr = external_server.recvfrom(1024)
        if not external_data:
            break
        relay_server.sendto(external_data, browser_addr)

    external_server.close()

relay_server.close()
