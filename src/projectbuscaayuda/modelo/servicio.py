import enum

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from .declarative_base import Base

class Categoria_Servicio(enum.Enum):

    PLOMERIA = 1
    CERRAJERIA = 2
    SASTRERIA = 3
    JARDINERIA = 4
    TAPICERIA = 5
    CARPINTERIA = 6
    ELECTRICIDAD = 7
    VENTANERIA = 8
    LAVADO_DE_ROPA = 9
    CONDUCCION_DE_AUTO = 10
    PLANCHADO_DE_ROPA = 11
    LAVADO_DE_AUTO = 12

class Servicio(Base):
    __tablename__ = 'servicio'

    id = Column(Integer, primary_key=true)
    descripcion = Column(String)
    categoria_servicio = Column(Enum(Categoria_Servicio))
    personas = relationship('Persona', secondary = 'servicio_persona')