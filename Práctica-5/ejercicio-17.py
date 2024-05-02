# a) Definir una función que permita el ingreso de números por teclado hasta ingresar el 0, y retorne esa lista.
# b) Definir una función que reciba como parámetro una lista de números y retorne como resultado el promedio.
# c) Definir una función que reciba como parámetro una lista de números y retorne como resultado la suma de los números.
# d) Definir una función que reciba como parámetro una lista de números y retorne el número más grande de la lista (máximo).
# e) Definir una función que reciba como parámetro una lista de números y retorne el número más pequeño de la lista (mínimo).
# f) Definir una función denominada porcentaje, que tenga 2 parámetros formales, que representan el total y un valor y retorna el porcentaje de ese valor respecto del total.

# Utilizar las funciones definidas anteriormente para construir un programa que permita elegir una opción del siguiente menú, el cuál debe mostrarse permanentemente hasta que se elija la opción 7:

# 1. Ver el promedio de los números
# 2. Ver la suma de los números
# 3. Ver la cantidad de números
# 4. Ver el número máximo
# 5. Ver el número mínimo
# 6. Calcular porcentaje
# 7. Salir 

# Recordar que el promedio de números se calcula como la suma sobre la cantidad.

def ingreso_numeros():
    numeros = []
    while True:
        numero = float(input("Ingrese un número (0 para terminar): "))
        if numero == 0:
            break
        numeros.append(numero)
    return numeros

def promedio(numeros):
    suma = sum(numeros)
    cantidad = len(numeros)
    return suma / cantidad

def suma(numeros):
    return sum(numeros)

def maximo(numeros):
    return max(numeros)

def minimo(numeros):
    return min(numeros)

def porcentaje(total, valor):
    return (valor / total) * 100

def mostrar_menu():
    numeros = []
    while True:
        print("Menú de opciones")
        print("1. Ver el promedio de los números")
        print("2. Ver la suma de los números")
        print("3. Ver la cantidad de números")
        print("4. Ver el número máximo")
        print("5. Ver el número mínimo")
        print("6. Calcular porcentaje")
        print("7. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            if numeros:
                prom = promedio(numeros)
                print("El promedio de los números es: " + (prom))
            else:
                print("La lista de números está vacía.")
        elif opcion == 2:
            if numeros:
                s = suma(numeros)
                print("La suma de los números es: " + str(s))
            else:
                print("La lista de números está vacía.")
        elif opcion == 3:
            cantidad = len(numeros)
            print("La cantidad de números es: " + str(cantidad))
        elif opcion == 4:
            if numeros:
                max_num = maximo(numeros)
                print("El número máximo es: " + str(max_num))
            else:
                print("La lista de números está vacía.")
        elif opcion == 5:
            if numeros:
                min_num = minimo(numeros)
                print("El número mínimo es: "+ str(min_num))
            else:
                print("La lista de números está vacía.")
        elif opcion == 6:
            if numeros:
                total = float(input("Ingrese el valor total: "))
                valor = float(input("Ingrese el valor a calcular el porcentaje: "))
                porc = porcentaje(total, valor)
                print("El porcentaje es: " + str(porc))
            else:
                print("La lista de números está vacía.")
        elif opcion == 7:
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

        print() # Espacio en blanco para mayor claridad.

mostrar_menu()

# Este programa utiliza todas las funciones definidas en los ejercicios anteriores para permitir al usuario elegir opciones del menú y realizar diferentes cálculos sobre una lista de números.