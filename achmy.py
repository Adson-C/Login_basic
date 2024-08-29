from pathlib import Path

from sqlalchemy import create_engine, String, Boolean, select
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
    **kwargs
):
    with Session(bind=engine) as session:
        user = Usuario(
            nome = nome,
            senha = senha,
            email = email,
            **kwargs
        )
        session.add(user)
        session.commit()
        
# Leitura =============================================================================
def ler_todos_usuarios():
    with Session(bind=engine) as session:
        comando_sql = select(Usuario)
        usuarios = session.execute(comando_sql).fetchall()
        usuarios = [usuario[0] for usuario in usuarios]
        return usuarios
    
# ler por ID do usuario
def ler_por_id(id):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuario = session.execute(comando_sql).fetchall()
        return usuario[0][0]
        
if __name__ == '__main__':
    # criar_usuarios(
    #     'Gisslle Pimentel',
    #     senha='admin',
    #     email= 'adson@example.com',
    #     # acesso_gestor=True
    #)
    
    # usuarios = ler_todos_usuarios()
    # usuario_0 = usuarios[0]
    # print(usuario_0)
    # print(usuario_0.nome, usuario_0.email, usuario_0.senha)
    
    usuario_1 = ler_por_id(id=3)
    print(usuario_1)
    print(usuario_1.nome, usuario_1.email, usuario_1.senha)