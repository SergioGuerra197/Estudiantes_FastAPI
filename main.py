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
        'id':123456789,
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

@app.put('/estudiantes/{id}',tags=['CRUD'])
def actualizar_estudiante(id: int, estudiante: Estudiante):
    for item in estudiantes:
        if item['id'] == id:
            item['nombre'] = estudiante.nombre
            item['apellido'] = estudiante.apellido
            item['direccion'] = estudiante.direccion
            item['carrera'] = estudiante.carrera
            item['semestre'] = estudiante.semestre
            return JSONResponse(content={'message':'Se actualizó el estudiante'})

@app.delete('/estudiantes/{id}', tags=['CRUD'])
def eliminar_estudiante(id: int):
    for item in estudiantes:
        if item['id'] == id:
            estudiantes.remove(item)
            return JSONResponse(content = {'message':'Se elimino el estudiante'})