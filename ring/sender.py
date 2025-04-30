#!d:\Python\Python312\python.exe

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.1', 1234))
clientsocket.send(str(2).encode())
clientsocket.close()