import socket

HOST_NAME = 'localhost'
PORT = 5223

s = socket.socket()
s.bind((HOST_NAME, PORT))

s.listen()

def client():
    conn, addr = s.accept()
    print('client connected from :', addr)
    return conn
