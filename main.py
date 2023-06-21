from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from clase_estudiante import *
from pydantic import Field
from typing import Optional, List


app = FastAPI()
app.title = 'Estudiantes'
app.version = '0.0.1'


estudiantes=[

]

@app.get('/estudiantes',tags=['CRUD'])
def listar_estudiantes():
    return JSONResponse(status_code=200, content=estudiantes)

@app.post('/estudiantes',tags=['CRUD'])
def agregar_estudiante(estudiante : Estudiante):
    estudiantes.append(estudiante)
    return JSONResponse(content={'message':'Se registro el estudiante'})