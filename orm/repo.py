import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

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

