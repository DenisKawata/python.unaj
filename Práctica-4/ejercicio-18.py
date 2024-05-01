# Una carnicería pasó de cobrar el vacío de $810 a $1044,90, ¿se puede saber de cúanto fue el porcentaje de aumento? si es así calculalo.

# DEFINIR UNA FUNCIÓN que reciba dos números y que retorne cuál es el porcentaje de aumento.

def calcular_porcentaje_aumento(valor_anterior, valor_actual):
    aumento = valor_actual - valor_anterior
    porcentaje_aumento = (aumento / valor_anterior) * 100
    return porcentaje_aumento

valor_anterior = 810
valor_actual = 1044.90

porcentaje_aumento = calcular_porcentaje_aumento(valor_anterior, valor_actual)

print("El porcentaje de aumento fue: " + str(porcentaje_aumento))

# En este código, se define una función llamada calcular_porcentaje_aumento que recibe dos números como parámetros: el valor anterior y el valor actual. Dentro de la función, se calcula la diferencia de aumento restando el valor anterior al valor actual. Luego, se calcula el porcentaje de aumento dividiendo esta diferencia de aumento entre el valor anterior y multiplicándolo por 100.

# Luego, se utiliza la función calcular_porcentaje_aumento para calcular y mostrar el porcentaje de aumento entre los valores dados: $810 y $1044.90.