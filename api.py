from fastapi import FastAPI, Depends
import orm.repo as repo
from sqlalchemy.orm import Session
from orm.config import generador_sesion
import orm.esquemas as esquemas

app = FastAPI()

# decorator
@app.get("/")
def hola_mundo():
    print("invocand# a ruta /")
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

# Busca alumn# por ID
# get("/alumnos/{id})
@app.get("/alumnos/{id}")
def alumno_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consulta alumn# por ID")
    return repo.alumno_por_id(sesion, id)

# Muestra calificaciones por ID de alumno
# get("/alumnos/{id}/calificaciones")
@app.get("/alumnos/{id}/calificaciones")
def calificaciones_por_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consulta calificaciones del alumn# ", id)
    return repo.calificacion_por_alumno(sesion,id)

# Muestra fotos por ID de alumno
# get("/alumnos/{id}/fotos")
@app.get("/alumnos/{id}/fotos")
def fotos_por_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consulta fotos del alumn# ",id)
    return repo.foto_por_alumno(sesion,id)

# Busca fot# por ID
# get("/fotos/{id}”)
@app.get("/fotos/{id}")
def foto_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consulta fot# por ID")
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
@app.delete("/alumnos/{id}/fotos")
def eliminar_fotos_por_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    repo.borrar_fotos_por_alumno(sesion,id)
    return {"foto_alumno_borrada", "ok"}

# Eliminar alumnos por ID
@app.delete("/alumnos/{id}")
def eliminar_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    repo.borrar_califs_por_alumno(sesion,id)
    repo.borrar_fotos_por_alumno(sesion,id)
    repo.borrar_alumno(sesion,id)
    return {"alumno_borrado", "ok"}


# post("/alumnos”)
@app.post("/alumnos")
def guardar_alumno(alumno:esquemas.AlumnoBase,sesion:Session=Depends(generador_sesion)):
    print(alumno)
    return repo.guardar_alumno(sesion,alumno)

# put("/alumnos/{id})
@app.put("/alumnos/{id}")
def actualizar_alumno(id:int,info_alumno:esquemas.AlumnoBase,sesion:Session=Depends(generador_sesion)):
    return repo.actualiza_alumno(sesion,id,info_alumno)

# post("/alumnos/{id}/calificaciones")
@app.post("/alumnos/{id}/calificaciones")
def guardar_calificacion(id:int,calificacion:esquemas.CalificacionBase,sesion:Session=Depends(generador_sesion)):
    print(calificacion)
    return repo.guardar_calificacion_por_alumno(sesion,id,calificacion)

# put("/calificaciones/{id}")
@app.put("/calificaciones/{id}")
def actualizar_calificacion(id:int,info_calificacion:esquemas.CalificacionBase,sesion:Session=Depends(generador_sesion)):
    return repo.actualiza_calificacion(sesion,id,info_calificacion)

# post("/alumnos/{id}/fotos")
@app.post("/alumnos/{id}/fotos")
def guardar_foto(id:int,foto:esquemas.FotoBase,sesion:Session=Depends(generador_sesion)):
    print(foto)
    return repo.guardar_foto_por_alumno(sesion,id,foto)

# put("/fotos/{id}")
@app.put("/fotos/{id}")
def actualizar_foto(id:int,info_foto:esquemas.FotoBase,sesion:Session=Depends(generador_sesion)):
    return repo.actualiza_foto(sesion,id,info_foto)