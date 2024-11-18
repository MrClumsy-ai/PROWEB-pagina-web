from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class PublicacionBase(BaseModel):
    Titulo: str
    IdUsuario: int
    Descripcion: str

class UsuarioBase(BaseModel):
    IdRol: int
    Nombre: str
    Contrasena: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]