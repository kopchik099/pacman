import sqlalchemy
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as dec
from sqlalchemy.orm import Session

sqlalchemybase = dec.declarative_base()
factory = None

def global_init(file):
    global factory
    con = f"sqlite:///{file.strip()}?check_same_thread=False"
    engine = sqlalchemy.create_engine(con, echo = False)
    factory = orm.sessionmaker(bind = engine)
    from . import all_models
    sqlalchemybase.metadata.create_all(engine)
def create_session()->Session:
    global factory
    return factory()