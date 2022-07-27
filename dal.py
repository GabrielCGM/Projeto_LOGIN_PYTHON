from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

#RETORNA A CONEXÃO
def return_engine():
    enginee = create_engine(conexao_bd, echo=False)
    return enginee
    

def return_session(user,senha,host,banco,port):
    
    try:
        global conexao_bd
        conexao_bd = f'mysql+pymysql://{user}:{senha}@{host}:{port}/{banco}'
        enginee = create_engine(conexao_bd, echo=False)
        Session = sessionmaker(bind=enginee)
    
    except Exception as e:
        print(f'NÃO FOI POSSIVEL CONECTAR AO BANCO DE DADOS >> {e}')
    
    else:
        print("""\033[33;40m
====================================
|MENSAGEM--> CONECTADO COM SUCESSO |
====================================
\033[m""")

        return Session()

#Tabela CADASTRO
class Cadastro(Base):
    __tablename__ = 'CADASTRO'
    id = Column(Integer, primary_key=True)
    nome = Column(String(20))
    email = Column(String(30))
    senha = Column(String(100))
    





