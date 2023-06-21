from pydantic import BaseModel, Field


class estudiante(BaseModel):
    id: int | None = None
    nombre: str
    apellido: str
    direccion: str
    carrera: str
    semestre: int 

    class Config:
        schema_extra={
            'ejemplo':{
                'id':1000888999,
                'nombre': 'Pepito',
                'apellido': 'Perez',
                'direccion': 'Cra 125c #00d 69',
                'carrera': 'Ingenieria Informatica',
                'semestre': 6
            }
        }