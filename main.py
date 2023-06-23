from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from clase_estudiante import *
from pydantic import Field
from typing import Optional, List


app = FastAPI()
app.title = 'Estudiantes'
app.version = '0.0.1'


estudiantes=[
    {
        'id':10005898,
        'nombre': 'Isabella',
        'apellido': 'Guerra',
        'direccion': 'luna del campo',
        'carrera': 'Medicina',
        'semestre': 1
    }
]

@app.get('/estudiantes',tags=['CRUD'])
def listar_estudiantes():
    return JSONResponse(status_code=200, content=estudiantes)

@app.post('/estudiantes',tags=['CRUD'])
def agregar_estudiante(estudiante : Estudiante):
    estudiantes.append(estudiante)
    return JSONResponse(content=estudiantes)