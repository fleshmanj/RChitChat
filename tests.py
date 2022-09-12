import time

import pytest
from client import User

ipaddress = "127.0.0.1"

# def test_connection():
#     u1 = User("Joshua", 1223)
#     u2 = User("Adam", 1224)


def test_recieve_data():
    u1 = User("Joshua")
    u2 = User("Adam")
    u1.make_connection(ipaddress, 1224)
    u2.make_connection(ipaddress, 1223)
    u1.send_message("\nHello from u1")
    u2.send_message("\nHello from u2")



