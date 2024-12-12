from orm.config import BaseClass
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
import datetime

class Alumno(BaseClass):
    __tablename__="alumnos"
    id=Column(Integer, primary_key=True)
    nombre=Column(String(100))
    edad=Column(Integer)
    domicilio=Column(String(100))
    carrera=Column(String(100))
    trimestre=Column(String(100))
    email=Column("email",String(100))
    password=Column(String(100))
    fecha_registro=Column(DateTime(timezone=True),default=datetime.datetime.now)

class Calificacion(BaseClass):
    __tablename__="calificaciones"
    id=Column(Integer, primary_key=True)
    id_alumno=Column(Integer, ForeignKey(Alumno.id))
    uea=Column(String(100))
    calificacion=Column(Integer)

class Foto(BaseClass):
    __tablename__="fotos"
    id=Column(Integer, primary_key=True)
    id_alumno=Column(Integer, ForeignKey(Alumno.id))
    titulo=Column(String(100))
    descripcion=Column(String(100))
    ruta=Column(String(50))
