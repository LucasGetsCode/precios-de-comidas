from typing import TypedDict, Union

class MiDict(TypedDict):
    precio: Union[int, float]
    nombre: str
    edad: int

def mi_funcion() -> MiDict:
    return {
        "precio": 100,
        "nombre": "Producto",
        "edad": 30
    }

resultado = mi_funcion()
print(resultado)