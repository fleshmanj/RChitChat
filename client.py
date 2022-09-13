import threading
from settings import PORT
from connection import Sconnection


class User:

    def __init__(self,port):
        self.sock_out = None
        self.connection = Sconnection(port)
        # for i, node in enumerate(NODES):
        #     self.connection.connect((NODES[i], PORT))
        t = threading.Thread(target=self.connection.recv, daemon=True)
        t.start()

    def get_user_input(self):
        command = input(f"({self.connection.host_port}) ")
        if command == "/c":
            temp = input("Add ip address and port to send to i.e. 0.0.0.0\n")
            temp = temp.split(":")
            self.connection.nodes.append((temp[0], int(temp[1])))
        if command == "q":
            return False
        if len(command) > 1 and command != "/c":
            self.connection.send(command)
        return True

    def main(self):
        print("Running main")
        run = True
        while run:
            self.get_user_input()


if __name__ == "__main__":
    user = User(1223)
    user.main()
