# Escribir un programa que dado un año determine si es bisiesto o no. Un año es bisiesto si es múltiplo de 4. Los años múltiplos de 100 no son  bisiestos, salvo si ellos son también múltiplos de 400 (2000 es bisiesto, pero 1800 no lo es).

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        return True
    else:
        return False

anio = int(input("Ingrese un año: "))

if es_bisiesto(anio):
    print("El año " + str(anio) + " es bisiesto.")
else:
    print("El año " + str(anio) + " no es bisiesto.")

# En este código, se define una función llamada es_bisiesto que recibe un año como parámetro. Dentro de la función, se verifica si el año cumple con las condiciones para ser considerado bisiesto: debe ser divisible por 4, pero no por 100, a menos que también sea divisible por 400. Si se cumplen estas condiciones, la función retorna True, indicando que el año es bisiesto. En caso contrario, retorna False.

# Después, se solicita al usuario que ingrese un año. Se llama a la función es_bisiesto con el año ingresado y se determina si es bisiesto o no. Finalmente, se muestra en pantalla si el año es bisiesto o no.