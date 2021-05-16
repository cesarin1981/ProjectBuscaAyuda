from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Persona(Base):
    __tablename__ = 'persona'

    id = Column(Integer, primary_key=True)

    nombre = Column(String)
    apellido = Column(String)
    foto = Column(String)
    telefono = Column(String)
    correo = Column(String)

    servicio = relationship('Servicio', secondary = 'servicio_persona')

class Servicio_Persona(Base):
    __tablename__ = 'servicio_persona'

    persona = Column(Integer, ForeignKey('persona.id'), primary_key=True)
    servicio = Column(Integer, ForeignKey('servicio.id'), primary_key=True)
    year_experiencia = Column(Integer)
