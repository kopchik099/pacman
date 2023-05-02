import socket
import time
import pygame
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
sock.connect(('localhost', 10000))
pygame.init()
height = 500
width = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('пакман онлайн')
run = True
players = []
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    sock.send('лукас'.encode())
    data = sock.recv(1024).decode()
    print(f'получил: {data}')
    
pygame.quit()
