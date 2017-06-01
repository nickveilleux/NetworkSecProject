import socket
import subprocess


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print('Now Listening')
conn, addr = s.accept()
print ('Connection Address')

while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print ('Receieved Data:", data.decode())
        result = subprocess.run(["ifconfig", "-v"], stdout = subprocess.PIPE)
        print (result)
        conn.send(result.stdout)

conn.close
