import socket
HOST = 'localhost'    # The remote host
PORT = 50008              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
f = open("test.jpg", mode="br")
file = f.read()
print(type(file))
s.sendall(file)
data = s.recv(1024)
s.close()
f.close()
print('Received', repr(data))
