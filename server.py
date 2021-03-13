'''
	Execute server.py usando host1 e port1 como root!
'''
import socket
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host1 = socket.gethostname()
host2 = '127.0.0.1'
port1 = 80
port2 = 1234
serversocket.bind((host1,80))
# become a server socket
serversocket.listen(5)

while True:
	(clientsocket,address) = serversocket.accept()
	ct = client_thread(clientsocket)
	ct.run()
