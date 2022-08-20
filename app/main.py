from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/randomId/{number}")
def get_number(number: int):
    resultado = number*2022 + random.randint(1,10)
    return {
            "Numero":str(number),
            "Resultado":str(resultado)
            }
