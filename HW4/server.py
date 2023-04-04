import socket

def calculate(expression):
    tokens = expression.split()
    if len(tokens) != 3:
        return None
    try:
        op1 = int(tokens[0])
        op2 = int(tokens[2])
    except ValueError:
        return None
    if tokens[1] == '+':
        return op1 + op2
    elif tokens[1] == '-':
        return op1 - op2
    elif tokens[1] == '*':
        return op1 * op2
    elif tokens[1] == '/':
        if op2 == 0:
            return None
        else:
            return round(op1 / op2, 1)
    else:
        return None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from', addr)

    while True:
        expression_bytes = client.recv(1024)
        expression = expression_bytes.decode().strip()
        if expression == 'q':
            break
        result = calculate(expression)
        if result is None:
            client.send(b'Invalid expression.')
        else:
            result_bytes = str(result).encode()
            client.send(result_bytes)

    client.close()
