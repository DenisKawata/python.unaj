# Evelyn cobra mensualmente $22500 por ser empleada de comercio. De su sueldo debe destinar $6750 al pago de impuestos, $11250 para comida y $4500 para el colegio de su hija.

# ¿Qué porcentaje del sueldo destina al pago de impuestos?
# ¿Qué porcentaje del sueldo destina a la comida?
# ¿Qué porcentaje del sueldo destina al colegio de su hija?

# Programe los siguientes puntos:

# 1. Defina una función que reciba a una persona, con su sueldo, el monto a destinar en impuestos, en comida y para colegio y retorne el porcentaje que destina en impuestos. Use la función para calcular porcentajes anteriormente definida para la práctica anterior.
# 2. Defina una función que reciba a una persona, con su sueldo, el monto a destinar en impuestos, en comida y para colegio y retorne el porcentaje que destina en comida. Use la función para calcular porcentajes anteriormente definida para la práctica anterior.
# 3. Defina una función que reciba a una persona, con su sueldo, el monto a destinar en impuestos, en comida y para colegio y retorne el porcentaje que destina en colegio. Use la función para calcular porcentajes anteriormente definida para la práctica anterior.

def porcentaje(monto_total, monto_destinado):
    return (monto_destinado / monto_total) * 100

def porcentaje_impuestos(persona):
    return porcentaje(persona['sueldo'], persona['impuestos'])

def porcentaje_comida(persona):
    return porcentaje(persona['sueldo'], persona['comida'])

def porcentaje_colegio(persona):
    return porcentaje(persona['sueldo'], persona['colegio'])

def calcular_porcentajes(persona):
    porcentaje_imp = porcentaje_impuestos(persona)
    porcentaje_com = porcentaje_comida(persona)
    porcentaje_col = porcentaje_colegio(persona)
    return porcentaje_imp, porcentaje_com, porcentaje_col

persona = {
    'sueldo': 22500,
    'impuestos': 6750,
    'comida': 11250,
    'colegio': 4500
}

porcentaje_impuestos = porcentaje_impuestos(persona)
porcentaje_comida = porcentaje_comida(persona)
porcentaje_colegio = porcentaje_colegio(persona)

print("El porcentaje del sueldo destinado a impuestos es: " + str(porcentaje_impuestos))
print("El porcentaje del sueldo destinado a comida es: " + str(porcentaje_comida))
print("El porcentaje del sueldo destinado al colegio es: " + str(porcentaje_colegio))

# En este programa, se definen tres funciones: porcentaje, porcentaje_impuestos, porcentaje_comida y porcentaje_colegio. La función porcentaje calcula el porcentaje de un monto destinado con respecto a un monto total.

# Luego, la función porcentaje_impuestos recibe una persona como parámetro y utiliza la función porcentaje para calcular el porcentaje del sueldo destinado a impuestos.

# La función porcentaje_comida recibe una persona como parámetro y utiliza la función porcentaje para calcular el porcentaje del sueldo destinado a comida.

# La función porcentaje_colegio recibe una persona como parámetro y utiliza la función porcentaje para calcular el porcentaje del sueldo destinado al colegio.

# Por último, se crea un diccionario persona con los datos proporcionados en el enunciado y se utilizan las funciones definidas para calcular los porcentajes correspondientes. Luego, se imprimen los resultados en pantalla.