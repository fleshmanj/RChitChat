import socket

hostname = "127.0.0.1"

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind((hostname, 8080))

serv.listen(5)

while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data
        print(from_client)
        conn.send("I am SERVER")
    conn.close()
    print('client disconnected')
