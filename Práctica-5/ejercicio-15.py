# Escriba un programa que le muestre a la persona usuaria el siguiente menú de opciones. El mismo debe estar siempre activo y, de acuerdo a la opción elegida, le solicite los datos restantes para imprimir el área de la figura elegida: 

# Menú de opciones 

# 1.- Círculo 
# 2.- Cuadrado 
# 3.- Rectángulo 
# 4.- Salir 

# Nota: asuma que cada una de las opciones es una función que recibe los argumentos/parameros necesarios para resolver el cálculo.

import math

def mostrar_menu():
    while True:
        print("Menú de opciones")
        print("1.- Círculo")
        print("2.- Cuadrado")
        print("3.- Rectángulo")
        print("4.- Salir")
        
        opcion = int(input("Ingrese una opción: "))
        
        if opcion == 1:
            radio = float(input("Ingrese el radio del círculo: "))
            area = math.pi * radio**2
            print("El área del círculo es:", area)
        elif opcion == 2:
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = lado**2
            print("El área del cuadrado es:", area)
        elif opcion == 3:
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = base * altura
            print("El área del rectángulo es:", area)
        elif opcion == 4:
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

mostrar_menu()

# En este programa, utilizamos un bucle while True para mantener el menú activo. La persona usuaria puede elegir una opción ingresando el número correspondiente. Según la opción elegida, se solicitan los datos necesarios para calcular el área de la figura correspondiente (círculo, cuadrado o rectángulo). Luego, se calcula el área y se imprime en pantalla.

# Si la persona usuaria elige la opción 4, el bucle se interrumpe y el programa termina.