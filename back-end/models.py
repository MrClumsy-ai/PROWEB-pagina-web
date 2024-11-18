from sqlalchemy import Column, Integer, String, BLOB, PrimaryKeyConstraint
from database import Base

class Usuario(Base):
    __tablename__ = "usuario"
    Id = Column(Integer, primary_key=True, index=True)
    IdRol = Column(Integer, nullable=False) # fk
    Nombre = Column(String(128), nullable=False)
    Contrasena = Column(String(128), nullable=False)
    FotoDePerfil = Column(BLOB, nullable=True)

class Rol(Base):
    __tablename__ = "rol"
    Id = Column(Integer, primary_key=True, index=True)
    Descripcion = Column(String(128), nullable=False)

class Publicacion(Base):
    __tablename__ = "publicacion"
    Id = Column(Integer, primary_key=True, index=True)
    IdUsuario = Column(Integer, nullable=False) # fk
    Titulo = Column(String(256), nullable=True)
    Descripcion = Column(String(512), nullable=True)
    Imagen = Column(BLOB, nullable=False)

class Comentario(Base):
    __tablename__ = "comentario"
    Id = Column(Integer, primary_key=True, index=True)
    IdPublicacion = Column(Integer, nullable=False) # fk
    IdUsuario = Column(Integer, nullable=False) # fk
    Texto = Column(String(128), nullable=False)

class Hashtag(Base):
    __tablename__ = "hashtag"
    Id = Column(Integer, primary_key=True, index=True)
    Texto = Column(String(128), nullable=False)

class DetallePublicacionHashtag(Base):
    __tablename__ = "detallePublicacionHashtag"
    IdPublicacion = Column(Integer, nullable=False) # fk
    IdHashtag = Column(Integer, nullable=False) # fk
    __table_args__ = (
        PrimaryKeyConstraint(IdPublicacion, IdHashtag),
        {}
    )

class Likes(Base):
    __tablename__ = "likes"
    IdPublicacion = Column(Integer, nullable=False) # fk
    IdUsuario = Column(Integer, nullable=False) # fk
    __table_args__ = (
        PrimaryKeyConstraint(IdPublicacion, IdUsuario),
        {}
    )