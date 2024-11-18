from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    Id = Column(Integer, primary_key=True, index=True)
    IdRol = Column(Integer) # fk
    Nombre = Column(String(128))

class Publicacion(Base):
    __tablename__ = "publicaciones"
    Id = Column(Integer, primary_key=True, index=True)
    IdUsuario = Column(Integer) # fk
    Titulo = Column(String(256))
    Descripcion = Column(String(512))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]