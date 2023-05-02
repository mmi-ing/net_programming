import socket
import binascii
import sys

ip = '220.69.189.125'
port = 443

save_ip = socket.getfqdn(ip)
save_port = socket.getservbyport(port)

print(save_ip)
print(save_port)
print(save_port+'://'+save_ip)
print(socket.inet_aton(ip))