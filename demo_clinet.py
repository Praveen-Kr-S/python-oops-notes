#Clinet side program
import socket
s = socket.socket()
host = socket.gethostname() #server system ip address -> ""
port = 8956
s.connect((host, port))
msg = s.recv(1024)
print(msg)
s.send(b"Hello Server, I am Sankar!!!")
s.close()
