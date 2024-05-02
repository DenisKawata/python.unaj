# Escriba un programa que le solicite al usuario que ingrese un monto de dinero y una opción del siguiente menú que debe mostrarse permanentemente hasta que se ingrese la opción D: 

# A: convertir_a_dolar 
# B: convertir_a_euro 
# C: convertir_a_real 
# D: salir 

# De acuerdo a la opción elegida, imprima cuanto equivale el monto en dólares, en euros y en reales. Utilizar las funciones ya definidas en el ejercicio 14 de la práctica 3 (convertir_a_dolar, convertir_a_euro y convertir_a_real).

def convertir_a_dolar(monto):
    return monto / 3.75

def convertir_a_euro(monto):
    return monto / 4.45

def convertir_a_real(monto):
    return monto / 0.65

def mostrar_menu():
    while True:
        print("Menú de opciones")
        print("A: convertir a dólar")
        print("B: convertir a euro")
        print("C: convertir a real")
        print("D: salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == 'A':
            monto = float(input("Ingrese el monto de dinero: "))
            monto_dolar = convertir_a_dolar(monto)
            print("El monto en dólares es: " + str(monto_dolar))
        elif opcion == 'B':
            monto = float(input("Ingrese el monto de dinero: "))
            monto_euro = convertir_a_euro(monto)
            print("El monto en euros es: " + str(monto_euro))
        elif opcion == 'C':
            monto = float(input("Ingrese el monto de dinero: "))
            monto_real = convertir_a_real(monto)
            print("El monto en reales es: " + str(monto_real))
        elif opcion == 'D':
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

mostrar_menu()

# En este programa, se definen tres funciones: convertir_a_dolar, convertir_a_euro y convertir_a_real, que realizan las conversiones de monto a dólar, euro y real respectivamente.

# La función mostrar_menu muestra el menú de opciones y solicita al usuario que ingrese una opción. Según la opción elegida, se solicita el monto de dinero y se realiza la conversión correspondiente utilizando las funciones definidas anteriormente. Luego, se imprime el monto convertido en la moneda seleccionada.

# Si el usuario elige la opción D, el bucle se interrumpe y el programa termina.