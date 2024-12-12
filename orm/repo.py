import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_
import orm.esquemas as esquemas

# SELECT * FROM app.alumnos
def alumnos_todos(sesion:Session):
    print("select * from app.alumnos")
    return sesion.query(modelos.Alumno).all()

# SELECT * FROM app.alumnos WHERE id={id_al}
def alumno_por_id(sesion:Session,id_alumno:int):
    print("select * from app.alumnos where id=", id_alumno)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id_alumno).first()

# SELECT * FROM app.fotos
def fotos_todos(sesion:Session):
    print("select * from app.fotos")
    return sesion.query(modelos.Foto).all()

# SELECT * FROM app.fotos WHERE id={id_fo}
def foto_por_id(sesion:Session,id_foto:int):
    print("select * from app.fotos where id=",id_foto)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_foto).first()

# SELECT * FROM app.fotos WHERE id_alumnos={id_al}
def foto_por_alumno(sesion:Session,id_alumno:int):
    print("select * from app.fotos where id_alumno=",id_alumno)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id_alumno).all()

# SELECT * FROM app.calificaciones
def calificaciones_todos(sesion:Session):
    print("select * from app.calificaciones")
    return sesion.query(modelos.Calificacion).all()

# SELECT * FROM app.calificaciones WHERE id={id_fo}
def calificacion_por_id(sesion:Session,id_calificacion:int):
    print("select * from app.calificaciones where id=",id_calificacion)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id==id_calificacion).first()

# SELECT * FROM app.calificaciones WHERE id_alumnos={id_al}
def calificacion_por_alumno(sesion:Session,id_alumno:int):
    print("select * from app.califcaciones where id_alumno=",id_alumno)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno==id_alumno).all()


# DELETE FROM app.alumnos WHERE id_alumnos={id_al}
def borrar_alumno(sesion:Session,id_alumno:int):
    print("delete from app.alumnos where id_alumno=",id_alumno)
    alumno = alumno_por_id(sesion,id_alumno)
    if alumno is not None:
        sesion.delete(alumno)
        sesion.commit()
    respuesta = { "mensaje": "alumno eliminado"}
    return respuesta

def borrar_foto(sesion:Session,id_foto:int):
    print("delete from app.fotos where id=",id_foto)
    foto = foto_por_id(sesion,id_foto)
    if foto is not None:
        sesion.delete(foto)
        sesion.commit()

def borrar_calificacion(sesion:Session,id_calificacion:int):
    print("delete from app.calificaciones where id=",id_calificacion)
    calificacion = calificacion_por_id(sesion,id_calificacion)
    if calificacion is not None:
        sesion.delete(calificacion)
        sesion.commit()

# DELETE FROM app.calificaciones WHERE id_alumnos={id_al}
def borrar_califs_por_alumno(sesion:Session,id_alumno:int):
    print("delete from app.calificaciones where id_alumno=",id_alumno)
    calificaciones_alu = calificacion_por_alumno(sesion,id_alumno)
    if calificaciones_alu is not None:
        for calificacion_alu in calificaciones_alu:
            sesion.delete(calificacion_alu)
        sesion.commit()

# DELETE FROM app.fotos WHERE id_alumnos={id_al}
def borrar_fotos_por_alumno(sesion:Session,id_alumno:int):
    print("delete from app.fotos where id_alumno=",id_alumno)
    fotos_alu = foto_por_alumno(sesion, id_alumno)
    if fotos_alu is not None:
        for foto_alumno in fotos_alu:
            sesion.delete(foto_alumno)
        sesion.commit()


def guardar_alumno(sesion:Session, alum_nuevo:esquemas.AlumnoBase):
    alum_bd = modelos.Alumno()
    alum_bd.nombre = alum_nuevo.nombre
    alum_bd.edad = alum_nuevo.edad
    alum_bd.domicilio = alum_nuevo.domicilio
    alum_bd.carrera = alum_nuevo.carrera
    alum_bd.trimestre = alum_nuevo.trimestre
    alum_bd.email = alum_nuevo.email
    alum_bd.password = alum_nuevo.password
    sesion.add(alum_bd)
    sesion.commit()
    sesion.refresh(alum_bd)
    return alum_bd

def actualiza_alumno(sesion:Session,id_alumno:int,alum_esquema:esquemas.AlumnoBase):
    alum_bd = alumno_por_id(sesion,id_alumno)
    if alum_bd is not None:
        alum_bd.nombre = alum_esquema.nombre
        alum_bd.edad = alum_esquema.edad
        alum_bd.domicilio = alum_esquema.domicilio
        alum_bd.carrera = alum_esquema.carrera
        alum_bd.trimestre = alum_esquema.trimestre
        alum_bd.email = alum_esquema.email
        alum_bd.password = alum_esquema.password
        sesion.commit()
        sesion.refresh(alum_bd)
        print(alum_esquema)
        return alum_esquema
    else:
        respuesta = {"mensaje":"No existe el alumno"}
        return respuesta

def guardar_calificacion_por_alumno(sesion:Session,id_alumno:int,cali_nuevo:esquemas.CalificacionBase):
    cali_sear = calificacion_por_alumno(sesion,id_alumno)
    if cali_sear is not None:
        cali_bd = modelos.Calificacion()
        cali_bd.id_alumno = id_alumno
        cali_bd.uea = cali_nuevo.uea
        cali_bd.calificacion = cali_nuevo.calificacion
        sesion.commit()
        sesion.refresh(cali_bd)
        return cali_bd

def actualiza_calificacion(sesion:Session,id_calificacion:int,cali_esquema:esquemas.CalificacionBase):
    cali_bd = calificacion_por_id(sesion,id_calificacion)
    if cali_bd is not None:
        cali_bd.uea = cali_esquema.uea
        cali_bd.calificacion = cali_esquema.calificacion
        sesion.commit()
        sesion.refreseh(cali_bd)
        print(cali_esquema)
        return cali_esquema
    else:
        respuesta = {"mensaje":"No existe califiacion"}
        return respuesta

def guardar_foto_por_alumno(sesion:Session,id_alumno:int,foto_nuevo:esquemas.FotoBase):
    foto_sear = foto_por_alumno(sesion,id_alumno)
    if foto_sear is not None:
        foto_bd = modelos.Foto()
        foto_bd.id_alumno = id_alumno
        foto_bd.titulo = foto_nuevo.titulo
        foto_bd.descripcion = foto_nuevo.descripcion
        foto_bd.ruta = foto_nuevo.ruta
        sesion.commit()
        sesion.refresh(foto_bd)
        return foto_bd

def actualiza_foto(sesion:Session,id_foto:int,foto_esquema:esquemas.FotoBase):
    foto_bd = foto_por_id(sesion,id_foto)
    if foto_bd is not None:
        foto_bd.tiulo = foto_esquema.titulo
        foto_bd.descripcion = foto_esquema.descripcion
        foto_bd.ruta = foto_esquema.ruta
        sesion.commit()
        sesion.refresh(foto_bd)
        print(foto_esquema)
        return foto_esquema
    else:
        respuesta = {"mensaje":"No existe la foto"}
        return respuesta
