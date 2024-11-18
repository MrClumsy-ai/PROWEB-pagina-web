from sqlalchemy import Boolean, Column, Integer, String, BLOB, PrimaryKeyConstraint
from database import Base

class Usuario(Base):
    __tablename__ = "usuario"
    Id = Column(Integer, primary_key=True, index=True)
    IdRol = Column(Integer) # fk
    Nombre = Column(String(128))
    Contrasena = Column(String(128))
    FotoDePerfil = Column(BLOB)

class Rol(Base):
    __tablename__ = "rol"
    Id = Column(Integer, primary_key=True, index=True)
    Descripcion = Column(String(128))

class Publicacion(Base):
    __tablename__ = "publicacion"
    Id = Column(Integer, primary_key=True, index=True)
    IdUsuario = Column(Integer) # fk
    Titulo = Column(String(256))
    Descripcion = Column(String(512))

class Comentario(Base):
    __tablename__ = "comentario"
    Id = Column(Integer, primary_key=True, index=True)
    IdPublicacion = Column(Integer) # fk
    Texto = Column(String(128))
    IdUsuario = Column(Integer) # fk

class Hashtag(Base):
    __tablename__ = "hashtag"
    Id = Column(Integer, primary_key=True, index=True)
    Texto = Column(String(128))

class DetallePublicacionHashtag(Base):
    __tablename__ = "detallePublicacionHashtag"
    IdPublicacion = Column(Integer) # fk
    IdHashtag = Column(Integer) # fk
    __table_args__ = (
        PrimaryKeyConstraint(IdPublicacion, IdHashtag)
    )

class Likes(Base):
    __tablename__ = "likes"
    IdPublicacion = Column(Integer) # fk
    IdUsuario = Column(Integer) # fk
    __table_args__ = (
        PrimaryKeyConstraint(IdPublicacion, IdUsuario)
    )