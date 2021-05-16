from src.projectbuscaayuda.modelo.persona import Persona
from src.projectbuscaayuda.modelo.servicio import Servicio, Categoria_Servicio
from src.projectbuscaayuda.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    session = Session()
    personas = session.query(Persona).all()
    print('Las personas que brindan servicios almacenadas son:')
    for persona in personas:
        print("Apellidos y nombres: " + persona.apellido + " " + persona.nombre)

        print("Telefono: " + persona.telefono)
        print("Correo: " + persona.correo)
        print("Foto: " + persona.foto)

        print("---------------------------")
        print("")

        session.close()