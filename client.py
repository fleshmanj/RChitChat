import threading
from settings import PORT, NODES
from connection import Sconnection


class User:

    def __init__(self, name):
        self.sock_out = None
        self.name = name
        self.connection = Sconnection()
        for i, node in enumerate(NODES):
            self.connection.connect((NODES[i], PORT))
        t = threading.Thread(target=self.connection.recv, daemon=True)
        t.start()

    def get_user_input(self):
        command = input("\nEnter a command\n")
        if command == "/c":
            temp = input("Enter the ip address and port to connect to i.e. 0.0.0.0\n")

        if command.startswith("/") == True:
            if len(command) > 1:
                self.connection.send(command)
        if command == "q":
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
