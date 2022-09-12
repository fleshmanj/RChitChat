import threading
from settings import PORT
from connection import Sconnection


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
            temp = input("Enter the ip address and port to connect to i.e. 0.0.0.0\n")
            self.connection.connect((temp, PORT))
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
