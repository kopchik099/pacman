import socket
import time
import pygame
import pygame as pg
import math
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
sock.connect(('localhost', 10000))
pygame.init()
height = 500
width = 500
yellow = (255, 255, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
x = 0
y = 0
xcor = 250
ycor = 250
old = (0, 0)
cc = width/2, height/2
radius = 50
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('пакман онлайн')
run = True
players = []
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
#       if event.type==pg.KEYDOWN:
#           if event.key==pg.K_LEFT:
#               x=-10
#               y=0
#           if event.key==pg.K_RIGHT:
#               x=10
#               y=0
#           if event.key==pg.K_UP:
#               x=0
#               y=-10
#           if event.key==pg.K_DOWN:
#               x=0
#               y=10
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        vector = pos[0] - cc[0], pos[1] - cc[1]
        lenvector = math.sqrt(vector[0]**2 + vector[1]**2) 
        vector = vector[0]/lenvector, vector[1]/lenvector
        if lenvector <= radius:
            vector = 0, 0
        if vector != old:
            old = vector
            message = f'<{vector[0]}, {vector[1]}>'
            sock.send(message.encode())

    

    #sock.send('лукас'.encode())
    data = sock.recv(1024).decode()
    print(f'получил: {data}')
    screen.fill(black)
    pygame.draw.circle(screen, yellow, cc, radius)
    pygame.display.update()    
    
    

    
pygame.quit()
