# Escribir un programa y las funciones necesarias para calcular el promedio de N números ingresados por el usuario. (AYUDA: al comenzar el programa debe preguntar la cantidad de números a ingresar, luego iterar y leer tantos números del teclado como se indicó al inicio.)

def calcular_promedio(cantidad):
    suma = 0
    for _ in range(cantidad):
        numero = float(input("Ingrese un número: "))
        suma += numero
    promedio = suma / cantidad
    return promedio

cantidad_numeros = int(input("Ingrese la cantidad de números a ingresar: "))
promedio = calcular_promedio(cantidad_numeros)
print("El promedio de los números ingresados es: " + str(promedio))

# En este programa, la función calcular_promedio recibe la cantidad de números a ingresar como parámetro. Luego, utiliza un bucle for para solicitar al usuario que ingrese cada número y los va sumando en la variable suma. Al finalizar el bucle, se calcula el promedio dividiendo la suma entre la cantidad de números ingresados y se retorna el resultado.

# En el programa principal, se solicita al usuario que ingrese la cantidad de números a ingresar y se llama a la función calcular_promedio con ese valor. Luego, se muestra el promedio calculado.