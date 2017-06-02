import socket
import subprocess


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print('Now listening')
conn, addr = s.accept()
print ('Connection address', addr)
temp = subprocess.run(["ifconfig", "-v"], stdout=subprocess.PIPE)
length = str(len(temp.stdout))
while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	print ("received data:", data.decode())
	result = subprocess.run(["ifconfig", "-v"],  stdout=subprocess.PIPE)
	#length = str(len(result.stdout))
	
	
	#print(result.stdout)
	#conn.send(length.encode())
	conn.send(result.stdout + length.encode())
#conn.send(length.encode())
conn.close

