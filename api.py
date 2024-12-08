from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo
from sqlalchemy.orm import Session
from orm.config import generador_sesion

app = FastAPI()

class AlumnoBase(BaseModel):
    nombre:Optional[str]=None
    edad:int
    domicilio:str

alumnos = [{
    "id": 0,
    "nombre": "Rosa Gonzáles",
    "edad": 36,
    "domicilio": "Av. 102, 53"
}, {
    "id": 1,
    "nombre": "Irene Rojas",
    "edad": 38,
    "domicilio": "Calle 33, 10"
}, {
    "id": 2,
    "nombre": "Israel Ortíz",
    "edad": 8,
    "domicilio": "Av. Reforma, 122"
}, {
    "id": 3,
    "nombre": "Ximena Ramírez",
    "edad": 10,
    "domicilio": "Av. Constituyentes, 41"
}]

# decorator
@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "hola practica REST!!!"
    }
    return respuesta

# Muestra todos los alumnos
# get("/alumnos”)
@app.get("/alumnos")
def lista_alumnos(sesion:Session=Depends(generador_sesion)):
    print("API consulta todos los usuarios")
    return repo.alumnos_todos(sesion)
# Muestra todas las calificaciones
@app.get("/calificaciones")
def lista_calificaciones(sesion:Session=Depends(generador_sesion)):
    print("API consulta todas las calificaciones")
    return repo.calificaciones_todos(sesion)
# Muestra todas las fotos
@app.get("/fotos")
def lista_fotos(sesion:Session=Depends(generador_sesion)):
    print("API consulta todas las fotos")
    return repo.fotos_todos(sesion)

# Busca alumno por ID
# get("/alumnos/{id})
@app.get("/alumnos/{id}")
def alumno_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consulta alumno por ID")
    return repo.alumno_por_id(sesion, id)

# Muestra calificaciones por ID de alumno
# get("/alumnos/{id}/calificaciones")
@app.get("/alumnos/{id}/calificaciones")
def calificaciones_por_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consulta calificaciones del alumno ", id)
    return repo.calificacion_por_alumno(sesion,id)

# Muestra fotos por ID de alumno
# get("/alumnos/{id}/fotos")
@app.get("/alumnos/{id}/fotos")
def fotos_por_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consulta fotos del alumno ",id)
    return repo.foto_por_alumno(sesion,id)

# Busca foto por ID
# get("/fotos/{id}”)
@app.get("/fotos/{id}")
def foto_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consulta foto por ID")
    return repo.foto_por_id(sesion,id)

# Busca calificaciones por ID
# get("/calificaciones/{id}”)
@app.get("/calificaciones/{id}")
def calificacion_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consulta calificacion por ID")
    return repo.calificacion_por_id(sesion,id)


# Elimina fotos por ID
# delete("/fotos/{id}”)
@app.delete("/fotos/{id}")
def eliminar_foto(id:int,sesion:Session=Depends(generador_sesion)):
    repo.borrar_foto(sesion,id)
    return {"foto_borrada", "ok"}

# Elimina calificaciones por ID
# delete("/calificaciones/{id}”)
@app.delete("/calificaciones/{id}")
def eliminar_calificacion(id:int,sesion:Session=Depends(generador_sesion)):
    repo.borrar_calificacion(sesion,id)
    return {"calificacion_borrada", "ok"}

# Elimina calificaciones por ID de alumno
# delete("/alumnos/{id}/calificaciones")
@app.delete("/alumnos/{id}/calificaciones")
def eliminar_calificaciones_por_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    repo.borrar_califs_por_alumno(sesion,id)
    return {"calificacion_alumno_borrada", "ok"}

# Eliminar fotos por ID de alumno
# delete("/alumnos/{id}/fotos")
def eliminar_fotos_por_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    repo.borrar_fotos_por_alumno(sesion,id)
    return {"foto_alumno_borrada", "ok"}

# Eliminar alumnos por ID
# delete("/alumnos/{id})
def eliminar_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    repo.borrar_califs_por_alumno(sesion,id)
    repo.borrar_fotos_por_alumno(sesion,id)
    repo.borrar_alumno(sesion,id)
    return {alumno_borrado}