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

    def __init__(self, port):
        super().__init__()
        self.host = HOSTNAME
        self.host_port = port
        self.connections_out = []
        self.nodes = []
        self.sock_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock_in.bind((self.host, self.host_port))
        self.sock_in.listen()
        self.message_header = self.make_message_header()

    def recv(self):
        while True:
            conn, addr = self.sock_in.accept()
            # self.connections_out[addr] = conn
            while True:
                data = conn.recv(4096)
                if data != b'':
                    outside_node = self.get_header(data)
                    if outside_node not in self.nodes:
                        self.nodes.append(outside_node)
                    self.message_handler(data)
                if data == b'':
                    conn.close()
                    break

    def connect(self, address):
        temp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        temp.connect(address)
        return temp

    def send(self, message: str):
        for node in self.nodes:
            connection = self.connect(node)
            message_to_send = self.message_header + message
            connection.send(message_to_send.encode())

    def make_message_header(self) -> str:
        header = f"{self.host}:{self.host_port}"
        header = format(len(header), "08b") + header
        return header

    def get_header(self, data):
        length_of_header = data[:8]
        length_of_header = int(length_of_header, 2)
        header = data[8:length_of_header + 8].decode()
        header = header.split(":")
        header = (header[0], int(header[1]))
        return header

    def message_handler(self, data):
        length_of_header = data[:8]
        length_of_header = int(length_of_header, 2)
        header = data[8:length_of_header + 8].decode()
        header = header.split(":")
        payload = data[8 + length_of_header:].decode()
        message = f"({header[1]}) {payload}"
        print(message)
