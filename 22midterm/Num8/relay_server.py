from socket import *

relay_server = socket(AF_INET, SOCK_STREAM)
relay_server.bind(('localhost', 9000))
relay_server.listen(1)

while True:
    browser, browser_addr = relay_server.accept()
    browser_data = browser.recv(1024)

    # #브라우저로부터 받은 HTTP 요청 메시지에서 호스트 이름 추출
    # host = None
    # for line in browser_data.split(b'\r\n'):
    #     if line.startswith(b'Host:'):
    #         host = line.split(b' ')[1].decode()
    #         break

    # #호스트 이름이 추출되지 않았을 경우 연결 종료
    # if host is None:
    #     browser.close()
    #     continue

    #브라우저로부터 받은 HTTP 요청 메시지를 외부 서버에 전송
    external_server = socket(AF_INET, SOCK_STREAM)
    external_server.connect(('www.daum.net', 80))
    # external_server.connect((host, 80))
    external_server.sendall(browser_data.replace(f'Host: localhost:9000'.encode(), f'Host: www.daum.net'.encode()))

    #외부 서버로부터 받은 HTTP 응답 메시지를 브라우저에게 전달
    while True:
        external_data = external_server.recv(1024)
        if not external_data:
            break
        browser.sendall(external_data)

    external_server.close()
    browser.close()