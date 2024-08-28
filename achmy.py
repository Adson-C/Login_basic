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

    # CRUD =============================================================================