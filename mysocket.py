class MySocket:
    def __init__(self,sock = None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self,host,port):
        self.sock.connect((host,port))

    def mysend(self,msg):
        total_sent = 0
        while total_sent < MSGLEN:
            sent = self.sock.send(msg[total_sent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            total_sent = total_sent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd,2048))
            if chunk == 'b':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)
