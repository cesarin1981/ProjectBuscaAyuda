from src.projectbuscaayuda.modelo.persona import Persona
from src.projectbuscaayuda.modelo.servicio import Servicio, Categoria_Servicio
from src.projectbuscaayuda.modelo.declarative_base import Session, engine, Base

class Coleccion():
    def __init__(self):
        Base.metadata.create_all(engine)

    def registrar_servicio(self, descripcion, categoria_servicio):
        busqueda = session.query(Servicio).filter(Servicio.descripcion == descripcion).all()
        if len(busqueda) == 0:
            servicio = Servicio(descripcion=descripcion,categoria_servicio=categoria_servicio)
            session.add(servicio)
            session.commit()
            return True
        else:
            return false

    def editar_servicio(self, servicio_id, descripcion, categoria_servicio):
        busqueda = session.query(Servicio).filter(Servicio.descripcion == descripcion, Servicio.id != servicio_id).all()
        if len(busqueda) == 0:
            servicio = session.query(Servicio).filter(Servicio.id == Servicio.id).first()
            servicio.descripcion = descripcion
            servicio.categoria_servicio = categoria_servicio
            session.commit()
            return True
        else:
            return false


    def ver_servicios_por_id(self, servicio_id):
        return session.query(Servicio).get(servicio_id).__dict__

    def ver_servicios(self):
        return session.query(Servicio).__dict__


    def registrar_persona(self, nombre, apellido, foto, telefono, correo):
        busqueda = session.query(Persona).filter(Persona.nombre == nombre, Persona.apellido == apellido).all()
        if len(busqueda) == 0:
            persona = Persona(nombre=nombre,apellido=apellido,foto=foto,telefono=telefono,correo=correo)
            persona.add(persona)
            session.commit()
            return True
        else:
            return false

    def editar_persona(self, persona_id, nombre, apellido, telefono, foto, correo):
        busqueda = session.query(Persona).filter(Persona.nombre == nombre, Persona.apellido == apellido, Persona.id != persona_id).all()
        if len(busqueda) == 0:
            persona = session.query(Persona).filter(Persona.id == Persona.id).first()
            persona.nombre = nombre
            persona.apellido = apellido
            persona.telefono = telefono
            persona.correo = correo
            persona.foto = foto
            session.commit()
            return True
        else:
            return false


    def ver_personas_por_id(self, persona_id):
        return session.query(Persona).get(persona_id).__dict__

    def ver_personas(self):
        return session.query(Persona).__dict__