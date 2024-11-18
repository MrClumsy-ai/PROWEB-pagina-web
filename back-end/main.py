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

# GET
@app.get("/usuarios/{usuario_id}", status_code=status.HTTP_200_OK, tags=["GET"])
async def get_usuario(usuario_id: int, db: db_dependency):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.Id == usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="usuario no encontrado")
    return db_usuario

@app.get("/roles/{rol_id}", status_code=status.HTTP_200_OK, tags=["GET"])
async def get_rol(rol_id: int, db: db_dependency):
    db_rol = db.query(models.Rol).filter(models.Rol.Id == rol_id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="rol no encontrado")
    return db_rol

@app.get("/publicaciones/{publicacion_id}", status_code=status.HTTP_200_OK, tags=["GET"])
async def get_publicacion(publicacion_id: int, db: db_dependency):
    db_publicacion = db.query(models.Publicacion).filter(models.Publicacion.Id == publicacion_id)
    if db_publicacion is None:
        raise HTTPException(status_code=404, detail="publicacion no encontrada")
    return db_publicacion

@app.get("/comentarios/{comentario_id}", status_code=status.HTTP_200_OK, tags=["GET"])
async def get_comentario(comentario_id: int, db: db_dependency):
    db_comentario = db.query(models.Comentario).filter(models.Comentario.Id == comentario_id)
    if db_comentario is None:
        raise HTTPException(status_code=404, detail="comentario no encontrada")
    return db_comentario

@app.get("/hashtags/{hashtag_id}", status_code=status.HTTP_200_OK, tags=["GET"])
async def get_hashtag(hashtag_id: int, db: db_dependency):
    db_hashtag = db.query(models.Hashtag).filter(models.Hashtag.Id == hashtag_id)
    if db_hashtag is None:
        raise HTTPException(status_code=404, detail="hashtag no encontrada")
    return db_hashtag

@app.get("/detalle_publicacion_hashtag/{publicacion_id}&{hashtag_id}", status_code=status.HTTP_200_OK, tags=["GET"])
async def get_detalle_publicacion_hashtag(publicacion_id: int, hashtag_id: int, db: db_dependency):
    db_pubhash = db.query(models.DetallePublicacionHashtag).filter(models.DetallePublicacionHashtag.IdPublicacion == publicacion_id, models.DetallePublicacionHashtag.IdHashtag == hashtag_id)
    if db_pubhash is None:
        raise HTTPException(status_code=404, detail="detalle publicacion hashtag no encontrado")
    return db_pubhash

@app.get("/likes/{publicacion_id}&{usuario_id}", status_code=status.HTTP_200_OK, tags=["GET"])
async def get_like(publicacion_id: int, usuario_id: int, db: db_dependency):
    db_like = db.query(models.Likes).filter(models.Likes.IdPublicacionId == publicacion_id, models.Likes.IdUsuario)
    if db_like is None:
        raise HTTPException(status_code=404, detail="like no encontrado")
    return db_like

# contadores
@app.get("/contadores/likes/{publicacion_id}", status_code=status.HTTP_200_OK, tags=["CONTADORES"])
async def get_num_likes(publicacion_id: int, db: db_dependency):
    """da la cantidad de likes que tiene una publicacion"""
    db_likes = db.query(models.Likes).filter(models.Likes.IdPublicacion == publicacion_id).count()
    if db_likes is None:
        raise HTTPException(status_code=404, detail="publicacion no encontrada")
    return db_likes

@app.get("/contadores/comentarios/{publicacion_id}", status_code=status.HTTP_200_OK, tags=["CONTADORES"])
async def get_num_comentarios(publicacion_id: int, db: db_dependency):
    """da la cantidad de comentarios que tiene una publicacion"""
    db_comentarios = db.query(models.Comentario).filter(models.Comentario.IdPublicacion == publicacion_id).count()
    if db_comentarios is None:
        raise HTTPException(status_code=404, detail="publicacion no encontrada")
    return db_comentarios

@app.get("/contadores/publicaciones/{usuario_id}", status_code=status.HTTP_200_OK, tags=["CONTADORES"])
async def get_num_publicaciones(usuario_id: int, db: db_dependency):
    """da la cantidad de publicaciones que ha hecho el usuario"""
    db_publicaciones = db.query(models.Publicacion).filter(models.Publicacion.IdUsuario == usuario_id).count()
    if db_publicaciones is None:
        raise HTTPException(status_code=404, detail="usuario no encontrado")
    return db_publicaciones

@app.get("/contadores/hashtags/{hashtag_id}", status_code=status.HTTP_200_OK, tags=["CONTADORES"])
async def get_num_hashtag(hashtag_id: int, db: db_dependency):
    """da la cantidad de veces que se ha utilizado el hashtag"""
    db_hashtag = db.query(models.Hashtag).filter(models.Hashtag.Id == hashtag_id).count()
    if db_hashtag is None:
        raise HTTPException(status_code=404, detail="usuario no encontrado")
    return db_hashtag

# POST
@app.post("/usuarios/", status_code=status.HTTP_201_CREATED, tags=["POST"])
async def crear_usuario(usuario: UsuarioBase, db: db_dependency):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()

@app.post("/roles/", status_code=status.HTTP_201_CREATED, tags=["POST"])
async def crear_rol(rol: RolBase, db: db_dependency):
    db_rol = models.Rol(**rol.dict())
    db.add(db_rol)
    db.commit()

@app.post("/publicaciones/", status_code=status.HTTP_201_CREATED, tags=["POST"])
async def crear_publicacion(publicacion: PublicacionBase, db: db_dependency):
    db_publicacion = models.Publicacion(**publicacion.dict())
    db.add(db_publicacion)
    db.commit()

@app.post("/comentarios/", status_code=status.HTTP_201_CREATED, tags=["POST"])
async def crear_comentario(comentario: ComentarioBase, db: db_dependency):
    db_comentario = models.Comentario(**comentario.dict())
    db.add(db_comentario)
    db.commit()

@app.post("/hashtags/", status_code=status.HTTP_201_CREATED, tags=["POST"])
async def crear_hashtag(hashtag: HashtagBase, db: db_dependency):
    db_hashtag = models.Comentario(**hashtag.dict())
    db.add(db_hashtag)
    db.commit()

@app.post("/detalle_publicacion_hashtag/", status_code=status.HTTP_201_CREATED, tags=["POST"])
async def crear_detalle_publicacion_hashtag(pubhash: DetallePublicacionHashtagBase, db: db_dependency):
    db_pubhash = models.DetallePublicacionHashtag(**pubhash.dict())
    db.add(db_pubhash)
    db.commit()

@app.post("/likes/", status_code=status.HTTP_201_CREATED, tags=["POST"])
async def crear_like(like: LikesBase, db: db_dependency):
    db_like = models.Likes(**like.dict())
    db.add(db_like)
    db.commit()

# DELETE
@app.delete("/usuarios/{usuario}", status_code=status.HTTP_200_OK, tags=["DELETE"])
async def borrar_usuario(usuario_id: int, db: db_dependency):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.Id == usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="rol no encontrado")
    db.delete(db_usuario)
    db.commit()

@app.delete("/roles/{rol_id}", status_code=status.HTTP_200_OK, tags=["DELETE"])
async def borrar_rol(rol_id: int, db: db_dependency):
    db_rol = db.query(models.Rol).filter(models.Rol.Id == rol_id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="rol no encontrado")
    db.delete(db_rol)
    db.commit()

@app.delete("/publicaciones/{publicacion_id}", status_code=status.HTTP_200_OK, tags=["DELETE"])
async def borrar_publicacion(publicacion_id: int, db: db_dependency):
    db_publicacion = db.query(models.Publicacion).filter(models.Publicacion.Id == publicacion_id)
    if db_publicacion is None:
        raise HTTPException(status_code=404, detail="publicacion no encontrada")
    db.delete(db_publicacion)
    db.commit()

@app.delete("/comentarios/{comentario_id}", status_code=status.HTTP_200_OK, tags=["DELETE"])
async def borrar_comentario(comentario_id: int, db: db_dependency):
    db_comentario = db.query(models.Comentario).filter(models.Comentario.Id == comentario_id)
    if db_comentario is None:
        raise HTTPException(status_code=404, detail="comentario no encontrada")
    db.delete(db_comentario)
    db.commit()

@app.delete("/hashtags/{hashtag_id}", status_code=status.HTTP_200_OK, tags=["DELETE"])
async def borrar_hashtag(hashtag_id: int, db: db_dependency):
    db_hashtag = db.query(models.Hashtag).filter(models.Hashtag.Id == hashtag_id)
    if db_hashtag is None:
        raise HTTPException(status_code=404, detail="hashtag no encontrada")
    db.delete(db_hashtag)
    db.commit()

@app.delete("/detalle_publicacion_hashtag/{publicacion_id}&{hashtag_id}", status_code=status.HTTP_200_OK, tags=["DELETE"])
async def borrar_detalle_publicacion_hashtag(publicacion_id: int, hashtag_id: int, db: db_dependency):
    db_pubhash = db.query(models.DetallePublicacionHashtag).filter(models.DetallePublicacionHashtag.IdPublicacion == publicacion_id, models.DetallePublicacionHashtag.IdHashtag == hashtag_id)
    if db_pubhash is None:
        raise HTTPException(status_code=404, detail="detalle publicacion hashtag no encontrada")
    db.delete(db_pubhash)
    db.commit()

@app.delete("/likes/{publicacion_id}&{usuario_id}", status_code=status.HTTP_200_OK, tags=["DELETE"])
async def borrar_like(publicacion_id: int, usuario_id: int, db: db_dependency):
    db_like = db.query(models.Likes).filter(models.Likes.IdPublicacion == publicacion_id, models.Likes.IdUsuario == usuario_id)
    if db_like is None:
        raise HTTPException(status_code=404, detail="hashtag no encontrada")
    db.delete(db_like)
    db.commit()
