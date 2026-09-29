import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("Server Listening")

server.bind(("0.0.0.0",2222))

server.listen(5)

conn,addr = server.accept()

print(f"Connected: {addr}")

data = conn.recv(1024)

print(data.decode())

conn.sendall(b"Hello ChatGPT")