from pydantic import BaseModel, Field
from typing import Optional

class Estudiante(BaseModel):
    id: int | None = None
    nombre: str = Field(min_length= 3, max_length=20)
    apellido: Optional[str] = Field(min_length= 3, max_length=20)
    direccion: str = Field(min_length= 5, max_length=50)
    carrera: str = Field(min_length= 4, max_length=20)
    semestre: int = Field(ge=1, le=14)

    class Config:
        schema_extra={
            'example':{
                'id':1000888999,
                'nombre': 'Pepito',
                'apellido': 'Perez',
                'direccion': 'Cra 125c #00d 69',
                'carrera': 'Ingenieria Informatica',
                'semestre': 6
            }
        }