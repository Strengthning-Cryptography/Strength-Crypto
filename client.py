import socket

HOST_NAME = 'localhost'
PORT = 5223

def connect():
    c = socket.socket()
    c.connect((HOST_NAME, PORT))
    return c

