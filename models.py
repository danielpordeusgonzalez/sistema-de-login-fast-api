from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

USER = 'root'
PASSWORD = ''
HOST = 'localhost'
PORT = '3306'
DB = 'fastapi'

CONN = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    user = Column(String(100))
    senha = Column(String(100))


class Token(Base):
    __tablename__ = 'token'
    id = Column(Integer, primary_key=True)
    id_pessoa = Column(Integer, ForeignKey('pessoa.id'))
    token = Column(String(100))
    data = Column(DateTime, default=datetime.datetime.utcnow()
)
    
Base.metadata.create_all(engine)
