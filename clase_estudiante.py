from pydantic import BaseModel, Field


class estudiante(BaseModel):
    id: int | None = None
    nombre: str
    apellido: str
    direccion: str
    carrera: str
    semestre: int 