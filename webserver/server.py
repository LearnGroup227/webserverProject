import socket

serv_sock = socket.socket(socket.AF_INET,      # задаём семейство протоколов 'Интернет' (INET)
                          socket.SOCK_STREAM,  # задаем тип передачи данных 'потоковый' (TCP)
                          proto=0)             # выбираем протокол 'по умолчанию' для TCP, т.е. IP
# print(type(serv_sock))  # <class 'socket.socket'>

# telnet 192.168.0.105 10000
serv_sock.bind(('192.168.0.105', 10000))
backlog = 10  # Размер очереди входящих подключений, т.н. backlog
serv_sock.listen(backlog)

while True:
    client_sock, client_addr = serv_sock.accept()
    # client = serv_sock.accept()
    # print(client, type(client), sep='\n')
    print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        data = client_sock.recv(1024)
        if not data:
            # Клиент отключился
            break
        print(data)
        client_sock.sendall(data)

    client_sock.close()