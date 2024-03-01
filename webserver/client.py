import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
client_sock.connect(('192.168.0.105', 53210))
while True:
    request = input()
    client_sock.sendall(bytes(request, 'utf-8'))
    if '!' in request:
        break


def get_server_data() -> str:
    data = bytes()
    while True:
        respond = client_sock.recv(1024)
        if not respond:
            break
        data += respond
    return data.decode('utf-8')


print(get_server_data())

# Вопрос: как понять, что сервер нам что-то отправляет (или не отправляет) без использования sock.recv()? 
#    или: как понять, что сервер больше не ждёт данных? (это менее реализуемо)
