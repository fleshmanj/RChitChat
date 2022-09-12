import socket
from settings import PORT, HOSTNAME
from abc import ABC, abstractmethod


class Connection(ABC):

    def __init__(self):
        ...

    @abstractmethod
    def send(self, message):
        ...

    @abstractmethod
    def connect(self, address):
        ...

    @abstractmethod
    def recv(self):
        ...


class Sconnection(Connection):

    def __init__(self):
        super().__init__()
        self.connections_out = []
        self.sock_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock_in.bind((HOSTNAME, PORT))
        self.sock_in.listen()

    def recv(self):
        while True:
            conn, addr = self.sock_in.accept()
            # self.connections_out[addr] = conn
            self.connections_out.append(conn)
            while True:
                data = conn.recv(4096)
                if data != b'':
                    print(f"received data from {addr}")
                    print(data.decode())

    def connect(self, address):
        temp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        temp.connect(address)
        self.connections_out.append(temp)

    def send(self, message: str):
        for connection in self.connections_out:
            connection.send(message.encode())
