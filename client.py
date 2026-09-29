import socket

con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

con.connect(("91.106.73.34",2222))

con.sendall(b"Hello ChatGPT")

data = con.recv(1024)

print(data.decode())