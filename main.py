import socket
import time
from data.players import Player
from data.db_session import global_init, create_session

class LocalPlayer:
    def __init__(self, id, name, adress, socket):
        self.id = id
        self.name = name
        self.adress = adress
        self.socket = socket
        self.x = 500
        self.y = 500
        self.speed_y = 0
        self.speed_x = 0
        self.speed_abs = 1
        self.error = 0
        self.size = 50
        self.db: Player = create_session().get(Player, self.id )


global_init('db.sqlite')

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
main_socket.bind(('localhost', 10000))
main_socket.setblocking(False)
main_socket.listen(5)

db_session = create_session()
print('сокет создан')
players = {}
while True:
    try:
        new_socket, addr = main_socket.accept()
        print(f'подключился {addr}')
        main_socket.setblocking(False)
        addr = f'({addr[0]}, {addr[1]})'
        player = Player('ikari', addr)
        db_session.merge(player)
        db_session.commit()
        user = db_session.query(Player).filter(Player.adress == addr).first()
        player = LocalPlayer(user.id, 'ikari', addr, new_socket)
        players[user.id] = player


    except BlockingIOError:
        pass
    for id in list(players):
        try:
            data = players[id].socket.recv(1024).decode()
            print(f'получил: {data}')
        except:
            pass
    for id in list(players):
        try:
            players[id].socket.send('штукатурка'.encode())
        except:
            players[id].socket.close()
            del players[id]
            db_session.query(Player).filter(Player.id == id).delete()
            db_session.commit()
            print('сокет закрыт')
            
        
    
    time.sleep(0.01)

