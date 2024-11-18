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
    # CAMBIAR
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

# usuarios
@app.post("/usuarios/", status_code=status.HTTP_201_CREATED)
async def crear_usuario(usuario: UsuarioBase, db: db_dependency):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()

@app.get("/usuarios/{usuario_id}", status_code=status.HTTP_200_OK)
async def get_usuario(usuario_id: int, db: db_dependency):
    usuario = db.query(models.Usuario).filter(models.Usuario.Id == usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="usuario no encontrado")
    return usuario

@app.delete("/usuarios/{usuario}")
async def borrar_usuario(usuario_id: int, db: db_dependency):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.Id == usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="rol no encontrado")
    db.delete(db_usuario)
    db.commit()

# roles
@app.post("/roles/", status_code=status.HTTP_201_CREATED)
async def crear_rol(rol: RolBase, db: db_dependency):
    db_rol = models.Rol(**rol.dict())
    db.add(db_rol)
    db.commit()

@app.get("/roles/{rol_id}")
async def get_rol(rol_id: int, db: db_dependency):
    rol = db.query(models.Rol).filter(models.Rol.Id == rol_id)
    if rol is None:
        raise HTTPException(status_code=404, detail="rol no encontrado")
    return rol

@app.delete("/roles/{rol_id}")
async def borrar_rol(rol_id: int, db: db_dependency):
    db_rol = db.query(models.Rol).filter(models.Rol.Id == rol_id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="rol no encontrado")
    db.delete(db_rol)
    db.commit()

# publicaciones
@app.post("/publicaciones/", status_code=status.HTTP_201_CREATED)
async def crear_publicacion(publicacion: PublicacionBase, db: db_dependency):
    db_publicacion = models.Publicacion(**publicacion.dict())
    db.add(db_publicacion)
    db.commit()

@app.get("/publicaciones/{publicacion_id}", status_code=status.HTTP_200_OK)
async def get_publicacion(publicacion_id: int, db: db_dependency):
    publicacion = db.query(models.Publicacion).filter(models.Publicacion.Id == publicacion_id)
    if publicacion is None:
        raise HTTPException(status_code=404, detail="publicacion no encontrada")
    return publicacion

@app.delete("/publicaciones/{publicacion_id}", status_code=status.HTTP_200_OK)
async def borrar_publicacion(publicacion_id: int, db: db_dependency):
    db_publicacion = db.query(models.Publicacion).filter(models.Publicacion.Id == publicacion_id)
    if db_publicacion is None:
        raise HTTPException(status_code=404, detail="publicacion no encontrada")
    db.delete(db_publicacion)
    db.commit()


# comentarios
@app.post("/comentarios/", status_code=status.HTTP_201_CREATED)
async def crear_comentario(comentario: ComentarioBase, db: db_dependency):
    db_comentario = models.Comentario(**comentario.dict())
    db.add(db_comentario)
    db.commit()

@app.get("/comentarios/{comentario_id}", status_code=status.HTTP_200_OK)
async def get_comentario(comentario_id: int, db: db_dependency):
    comentario = db.query(models.Comentario).filter(models.Comentario.Id == comentario_id)
    if comentario is None:
        raise HTTPException(status_code=404, detail="comentario no encontrada")
    return comentario

@app.delete("/comentarios/{comentario_id}", status_code=status.HTTP_200_OK)
async def borrar_comentario(comentario_id: int, db: db_dependency):
    db_comentario = db.query(models.Comentario).filter(models.Comentario.Id == comentario_id)
    if db_comentario is None:
        raise HTTPException(status_code=404, detail="comentario no encontrada")
    db.delete(db_comentario)
    db.commit()

# hashtags
@app.post("/hashtags/", status_code=status.HTTP_201_CREATED)
async def crear_hashtag(hashtag: HashtagBase, db: db_dependency):
    db_hashtag = models.Comentario(**hashtag.dict())
    db.add(db_hashtag)
    db.commit()

@app.get("/hashtags/{hashtag_id}", status_code=status.HTTP_200_OK)
async def get_hashtag(hashtag_id: int, db: db_dependency):
    hashtag = db.query(models.Hashtag).filter(models.Hashtag.Id == hashtag_id)
    if hashtag is None:
        raise HTTPException(status_code=404, detail="hashtag no encontrada")
    return hashtag

@app.delete("/hashtags/{hashtag_id}", status_code=status.HTTP_200_OK)
async def borrar_hashtag(hashtag_id: int, db: db_dependency):
    db_hashtag = db.query(models.Hashtag).filter(models.Hashtag.Id == hashtag_id)
    if db_hashtag is None:
        raise HTTPException(status_code=404, detail="hashtag no encontrada")
    db.delete(db_hashtag)
    db.commit()
