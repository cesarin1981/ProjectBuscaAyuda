from src.projectbuscaayuda.modelo.persona import Persona
from src.projectbuscaayuda.modelo.servicio import Servicio, Categoria_Servicio
from src.projectbuscaayuda.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':

    Base.metadata.create_all(engine)

    session = Session()

    persona1 = Persona(nombre = "Manuel", apellido = "Quintana", foto = "en proceso", telefono = "941952366", correo="manuelquintana55@gmail.com")
    persona2 = Persona(nombre = "Juan", apellido = "Castro Sotomayor", foto = "en proceso", telefono = "923955526", correo="soto.mayor.1@gmail.com")
    persona3 = Persona(nombre = "Marcos", apellido = "Contreras Lopez", foto = "en proceso", telefono = "943221121", correo="marcos111@gmail.com")

    session.add(persona1)
    session.add(persona2)
    session.add(persona3)
    session.commit()

    servicio1 = Servicio(descripcion = "corte, reparacion y creacion de objetos con madera", categoria_servicio = Categoria_Servicio.CARPINTERIA)
    servicio2 = Servicio(descripcion = "Reparacion e instalacion de servicios electricos", categoria_servicio = Categoria_Servicio.ELECTRICIDAD)
    session.add(servicio1)
    session.add(servicio2)

    servicio1.persona = [persona1]
    servicio2.persona = [persona2, persona3]

    session.commit()
    session.close()