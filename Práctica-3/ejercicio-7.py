# Definir una función que calcule el área de un circulo, otra ue calcule el área de un rectangulo y otra que calcule el área de un cuadrado. Analice qué parámetros deberian recibir dichas funciones.

import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

def calcular_area_cuadrado(lado):
    area = lado**2 
    return area

# ejemppo de uso de las funciones anteriores

print(calcular_area_circulo(5))
print(calcular_area_rectangulo(5, 10))
print(calcular_area_cuadrado(5))

# En este código, la Función CALCULAR_AREA_CIRCULO recibe un parámetro llamado RADIO. Para calcular el área de un círculo, necesitamos el radio.
# La función CALCULAR_AREA_RECTANGULO recibe dos parámetros: BASE y ALTURA. Para calcular el área de un rectángulo, necesitamos la base y la altura.
# En el caso de la función CALCULAR_AREA_CUADRADO, no recibe ningún parámetro. Para calcular el área de un cuadrado, necesitamos el lado.

# Luego, se muestra el uso de las funciones anteriores. 