from src.projectbuscaayuda.modelo.persona import Persona
from src.projectbuscaayuda.modelo.servicio import Servicio, Categoria_Servicio
from src.projectbuscaayuda.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    session = Session()
    persona1 = session.query(Persona).get(1)
    session.delete(persona1)
    session.commit()
    session.close()