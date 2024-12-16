from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import CONN, Pessoa, Token
from secrets import token_hex


app = FastAPI()

def conectaBanco():
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

@app.post("/cadastro")
def cadastro(nome: str, user: str, senha:str):
    session = conectaBanco()
    usuario = session.query(Pessoa).filter_by(user=user, senha=senha).all()
    if len(usuario) == 0:
        x = Pessoa(nome=nome, user=user, senha=senha)
        session.add(x)
        session.commit()
        return {"status": "sucesso"}
    else:
        {"status": "Error, usuario já cadastrado"}