import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('192.168.0.105', 53210))
while True:
    request = input()
    client_sock.sendall(bytes(request, 'utf-8'))
    if '!' in request:
        break
data = client_sock.recv(1024)
client_sock.close()
print(repr(data))