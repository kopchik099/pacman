import socket
import time
socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket2.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
socket2.connect(('localhost', 10000))
while True:
    socket2.send('говнядина'.encode())
    
