import socket
import threading
from settings import PORT,PORT_OUT, HOSTNAME, USERNAME
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
            while True:
                data = conn.recv(4096)
                if data != b'':
                    print(data.decode())

    def connect(self, address):
        temp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        temp.connect(address)
        self.connections_out.append(temp)
        pass

    def send(self, message: str):
        for connection in self.connections_out:
            connection.send(message.encode())


class User:

    def __init__(self, name):
        self.sock_out = None
        self.name = name
        self.connection = Sconnection()
        t = threading.Thread(target=self.connection.recv, daemon=True)
        t.start()


    def get_user_input(self):
        command = input("\nEnter a command\n")
        if command == "/c":
            temp = input("Enter the ip address and port to connect to i.e. 0.0.0.0:1234\n")
            temp = temp.split(":")
            print(temp)
            self.connection.connect((temp[0], PORT_OUT))
        if command == "/msg":
            temp = input()
            if len(temp) > 0:
                self.connection.send(temp)
        if command == "/q":
            return False
        return True

    def main(self):
        print("Running main")
        run = True
        while run:
            self.get_user_input()


if __name__ == "__main__":
    user = User("Joshua")
    user.main()
