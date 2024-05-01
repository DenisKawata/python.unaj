# DEFINIR UNA FUNCIÓN que permita ingresar dos números enteros y que calcule qué porcentaje representa el primer número del segundo.
# Por ejemplo, si la función reibe 25 y 200, deberá retornar 50, y que el 25% de 200 es 50.

# Complete usando la función anterior

# El 25% de 890 =
# El 10% de 12600 =
# El 35% de 12600 =
# El 125% de 890 = 

def calcular_porcentaje(numero1, numero2):
    porcentaje = (numero1 / numero2) * 100
    return porcentaje

# Calcular el 25% de 890
numero1 = 25
numero2 = 890
porcentaje_1 = calcular_porcentaje(numero1, numero2)
print("El 25% de 890 es: " + str(porcentaje_1))

# Calcular el 10% de 12600
numero1 = 10
numero2 = 12600
porcentaje_2 = calcular_porcentaje(numero1, numero2)
print("El 10% de 12600 es: " + str(porcentaje_2))

# Calcular el 35% de 12600
numero1 = 35
porcentaje_3 = calcular_porcentaje(numero1, numero2)
print("El 35% de 12600 es: " + str(porcentaje_3))

# Calcular el 125% de 890
numero1 = 125
numero2 = 890
porcentaje_4 = calcular_porcentaje(numero1, numero2)
print("El 125% de 890 es: " + str(porcentaje_4))

# En este código, se define una función llamada calcular_porcentaje que recibe dos números enteros como parámetros. Dentro de la función, se calcula el porcentaje dividiendo el primer número entre el segundo y multiplicándolo por 100.

# Luego, se utilizan llamadas a esta función para calcular los porcentajes solicitados:

# - Se calcula el 25% de 890, utilizando los números 25 y 890.
# - Se calcula el 10% de 12600, utilizando los números 10 y 12600.
# - Se calcula el 35% de 12600, utilizando los números 35 y 12600.
# - Se calcula el 125% de 890, utilizando los números 125 y 890.