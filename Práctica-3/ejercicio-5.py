# Definir jemplo: una función denominada CUANTOS_DIAS que reciba el número de mes como  parámetro y retorne la cantidad de días que posee. Ejemplo: cuantos_dias (1), deberia retornar 31. Ayuda: Pensar en tener una lista de la siguiente manera: [["enero", 31], ["febrero", 28], ...]

def cuantos_dias(numero_mes):
    meses = [
        ["enero", 31],
        ["febrero", 28],
        ["marzo", 31],
        ["abril", 30],
        ["mayo", 31],
        ["junio", 30],
        ["julio", 31],
        ["agosto", 31],
        ["septiembre", 30],
        ["octubre", 31],
        ["noviembre", 30],
        ["diciembre", 31]
    ]
    for i in range(len(meses)):
        if meses[i][0] == numero_mes:
            return meses[i][1]
    return None

cuantidad_dias = cuantos_dias("enero")

print(cuantidad_dias)

# En este código, la función CUANTOS_DIAS recibe el número de mes como parámetro y retorna la cantidad de días que posee. Luego, la variable cuantidad_dias almacena el valor devuelto por la función CUANTOS_DIAS. Finalmente, se imprime el valor de la variable cuantidad_dias.