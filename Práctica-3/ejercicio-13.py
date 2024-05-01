# Definir una función llamada A_PAGAR que reciba 4 números: la cantidad de personas, el monto gastado en bebida, el monto gatado en comida y el del alquiler del lugar, y retorne cuanto le toca pagar a cada uno.

def a_pagar(cantidad_personas, monto_bebida, monto_comida, monto_alquiler):
    total_gastado = monto_bebida + monto_comida + monto_alquiler
    monto_por_persona = total_gastado / cantidad_personas
    return monto_por_persona

# Ejemplo de uso de la función
cantidad_personas = 10
monto_bebida = 200
monto_comida = 500
monto_alquiler = 1000

monto_por_persona = a_pagar(cantidad_personas, monto_bebida, monto_comida, monto_alquiler)
print("A cada persona le toca pagar: " + str(monto_por_persona))

# En este código, la función a_pagar recibe los parámetros cantidad_personas, monto_bebida, monto_comida y monto_alquiler. Luego, se calcula el total gastado sumando los montos de bebida, comida y alquiler. A continuación, se divide el total gastado por la cantidad de personas para determinar cuánto le toca pagar a cada una. Finalmente, se devuelve el monto por persona.