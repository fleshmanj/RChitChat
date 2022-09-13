import time

import pytest
from client import User

ipaddress = "127.0.0.1"

# def test_connection():
#     u1 = User("Joshua", 1223)
#     u2 = User("Adam", 1224)


# def test_recieve_data():
#     u1 = User(1223)
#     u2 = User(1224)
#     u1.connection.connect((ipaddress, 1224))
#     print(f"\n{u1.connection.connections_out}\n")
#     print(f"\n{u2.connection.connections_out}")
#     # u2.connection.connect(ipaddress, 1223)
#     u1.connection.send("\nHello from u1")
#     u2.connection.send("\nHello from u2")
#
#
# def test_header():
#     u1 = User(1234)
#     header = u1.connection.message_header()
#     assert header == "127.0.0.1:1234"

def test_header_sent():
    u1 = User(1234)
    u2 = User(1224)
    u1.connection.connect((ipaddress, 1224))
    u1.connection.send("\nHello from u1")
    u2.connection.send("\nHello from u2")

