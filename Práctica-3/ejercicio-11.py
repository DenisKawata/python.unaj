# Definir una función llamada ARMO_CARTEL que reciba una cadena de caracteres (para nombre del producto) y do números (el precio anterior y el otro para el precio rebajado) e imprima un cartel de la siguiente forma:

# Atención!!! Gran rebaja para el el producto nombre (Recibido commo  parámetro)
# Antes: Precio anterior (dato ecibido como parámetro)
# Ahora: Precio rebajado (dato recibido como parámetro)

def armo_cartel (nombre, precio_anterior, precio_rebajado):
    print("Atención!!! Gran rebaja para el producto " + str(nombre))
    print("Antes: " + str(precio_anterior))
    print("Ahora: " + str(precio_rebajado))

armo_cartel("Cafe", 100, 50) 

# En este código, la función ARMO_CARTEL recibe tres parámetros: nombre, precio_anterior y precio_rebajado. Luego, imprime los datos en el formato indicado. 