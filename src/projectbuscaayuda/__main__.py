from src.modelo.persona import Persona
from src.modelo.servicio import Servicio, Categoria_Servicio
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':

    #crea base de datos
    Base.metadata.create_all(engine)

    #Abre la sesión
    session = Session()

    #crear persona
    persona1 = Persona(nombre = "Manuel", apellido = "Quintana", foto = "en proceso", telefono = "941952366", correo="manuelquintana55@gmail.com")
    persona2 = Persona(nombre = "Juan", apellido = "Castro Sotomayor", foto = "en proceso", telefono = "923955526", correo="soto.mayor.1@gmail.com")
    persona3 = Persona(nombre = "Marcos", apellido = "Contreras Lopez", foto = "en proceso", telefono = "943221121", correo="marcos111@gmail.com")

    session.add(persona1)
    session.add(persona2)
    session.commit()

    #Crear servicio
    servicio1 = Servicio(descripcion = "corte, reparación y creación de objetos con madera", categoria_servicio = Categoria_Servicio.CARPINTERIA)
    servicio2 = Servicio(descripcion = "Reparación e instalación de servicios electricos", categoria_servicio = Categoria_Servicio.ELECTRICIDAD)
    session.add(servicio1)
    session.add(servicio2)


    #Relacionar albumes con canciones
    persona1.servicio = [persona1, servicio2]
    persona2.servicio = [persona2, servicio1]


    session.commit()
    session.close()