# Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio aeróbico; la fórmula que se aplica cuando el sexo es femenino es: (220-edad)/10; si el sexo es masculino es: (210-edad)/10. RESUELVA UTILIZANDO FUNCIONES

def calcular_pulsaciones(edad, sexo):
    if sexo == "F":
        pulsaciones = (220 - edad) / 10
    elif sexo == "M":
        pulsaciones = (210 - edad) / 10
    else:
        pulsaciones = None
    return pulsaciones

edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (M/F): ")

pulsaciones = calcular_pulsaciones(edad, sexo)

if pulsaciones is not None:
    print("El número de pulsaciones por cada 10 segundos de ejercicio es: " + str(pulsaciones))

# En este código, se define una función llamada calcular_pulsaciones que recibe la edad y el sexo como parámetros. Dentro de la función, se verifica si el sexo es femenino ("F") o masculino ("M") y se aplica la fórmula correspondiente para calcular el número de pulsaciones por cada 10 segundos de ejercicio. Si el sexo no es válido, se retorna None.

# Después, se solicita al usuario que ingrese su edad y su sexo. Se llama a la función calcular_pulsaciones con los valores ingresados y se calcula el número de pulsaciones. Si el número de pulsaciones no es None, se muestra en pantalla.