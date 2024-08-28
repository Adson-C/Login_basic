from pathlib import Path

from sqlalchemy import create_engine, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# Criar uma tabela de usuários
# =======================================================================
pasta_atual = Path(__file__).parent
PATH_TO_DB = pasta_atual / 'bd_usuario.sqlite'

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ =  'usuarios'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    senha: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(50))
    acesso_gestor: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self):
        return f"Usuario: {self.id=} ({self.nome=})"

engine = create_engine(f"sqlite:///{PATH_TO_DB}")
Base.metadata.create_all(bind=engine)

# CRUD ====================================================================
def criar_usuarios(
    nome,
    senha,
    email,
    acesso_gestor = False
):
    with Session(bind=engine) as session:
        user = Usuario(
            nome = nome,
            senha = senha,
            email = email,
            acesso_gestor = acesso_gestor
        )
        session.add(user)
        session.commit()
        
if __name__ == '__main__':
    criar_usuarios(
        'John P Sá',
        senha='admin',
        email= 'john@example.com',
        acesso_gestor=True
        )