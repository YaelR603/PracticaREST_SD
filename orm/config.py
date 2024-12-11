from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_BASE_DATOS = "postgresql://leay:hola@localhost:5432/alumnos"

engine = create_engine(URL_BASE_DATOS,
                       connect_args={
                           "options": "-csearch_path=app"
                       })

SessionClass = sessionmaker(engine)
def generador_sesion():
    sesion = SessionClass()
    try:
        yield sesion
    finally:
        sesion.close()

BaseClass = declarative_base()