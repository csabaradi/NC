#!d:\Python\Python312\python.exe

import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('127.0.0.3', 3456))
serversocket.listen(5)
print("Node 3 is listening on port 2345...")

def send(num):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('127.0.0.1', 1234))
    clientsocket.send(str(num).encode())
    clientsocket.close() 

while True:
    conn, _ = serversocket.accept()
    data = conn.recv(16)
    if not data:
        conn.close()
        continue
    num = int(data.decode())
    print(f"Node 3 received: {num}")
    num += 1
    send(num)
    if num >= 100:
        conn.close()
        break
    
    time.sleep(1)
    conn.close() 