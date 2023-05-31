from sqlalchemy import Column, Integer, String
from .db_session import sqlalchemybase
class Player(sqlalchemybase):
    __tablename__ = 'players'
    id = Column(Integer, primary_key = True, autoincrement = True)
    adress = Column(String)
    name = Column(String(15))
    size = Column(Integer, default = 50)
    x = Column(Integer, default = 500)
    y = Column(Integer, default = 500)
    speed_y = Column(Integer, default = 0)
    speed_x = Column(Integer, default = 0)
    speed_abs = Column(Integer, default = 1)
    error = Column(Integer, default = 0)
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
    
    