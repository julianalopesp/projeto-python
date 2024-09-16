from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Car(BaseModel):
    id: int
    marca: str
    modelo: str
    ano: int

carros_db = [
    {"id": 1, "marca": "Toyota", "modelo": "Corolla", "ano": 2020},
    {"id": 2, "marca": "Honda", "modelo": "Civic", "ano": 2019},
    {"id": 3, "marca": "Ford", "modelo": "Mustang", "ano": 2021},
    {"id": 4, "marca": "Chevrolet", "modelo": "Camaro", "ano": 2022},
    {"id": 5, "marca": "Volkswagen", "modelo": "Golf", "ano": 2018},
    {"id": 6, "marca": "Tesla", "modelo": "Model 3", "ano": 2023},
    {"id": 7, "marca": "BMW", "modelo": "M3", "ano": 2020},
    {"id": 8, "marca": "Audi", "modelo": "A4", "ano": 2021},
    {"id": 9, "marca": "Mercedes-Benz", "modelo": "C-Class", "ano": 2019},
    {"id": 10, "marca": "Hyundai", "modelo": "Elantra", "ano": 2022},
]

@app.get("/carros", response_model=List[Car])
def listar_carros():
    return carros_db


@app.get("/carros/{car_id}", response_model=Car)
def obter_carro(car_id: int):
    for carro in carros_db:
        if carro["id"] == car_id:
            return carro
    raise HTTPException(status_code=404, detail="Carro não encontrado")


@app.post("/carros", response_model=Car)
def adicionar_carro(carro: Car):
    carros_db.append(carro.dict())
    return carro
    
