#Server side logic
import socket
s = socket.socket()
host = socket.gethostname()
port = 8956
s.bind((host,port))
s.listen(3)
while True:
    conn, addr = s.accept() #to allow the proper clinet to server
    print(addr)
    conn.send(b"Hello Sanker, I am Server...")
    msg = conn.recv(1024)
    print(msg)
    conn.close()