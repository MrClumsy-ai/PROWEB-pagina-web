from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class UsuarioBase(BaseModel):
    IdRol: int
    Nombre: str
    Contrasena: str
    FotoDePerfil: str

class RolBase(BaseModel):
    Descripcion: str

class PublicacionBase(BaseModel):
    Titulo: str
    IdUsuario: int
    Descripcion: str

class ComentarioBase(BaseModel):
    IdPublicacion: int
    Texto: str
    IdUsuario: int

class HashtagBase(BaseModel):
    Texto: str

class DetallePublicacionHashtagBase(BaseModel):
    IdPublicacion: int
    IdHashtag: int

class LikesBase(BaseModel):
    IdPublicacion: int
    IdUsuario: int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]