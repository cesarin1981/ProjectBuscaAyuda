from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Persona(Base):
    __tablename__ = 'persona'

    id = Column(Integer, primary_key=true)

    nombre = Column(String)
    apellido = Column(String)
    foto = Column(String)
    telefono = Column(String)
    correo = Column(String)

    servicio = relationship('Servicio', secondary = 'servicio_persona')

class Servicio_Persona(Base):
    __tablename__ = 'servicio_persona'

    persona_id = Column(Integer, foreignkey('persona.id'), primary_key=true)
    servicio_id = Column(Integer, foreignkey('servicio.id'), primary_key=true)
    year_experiencia = Column(Integer)
