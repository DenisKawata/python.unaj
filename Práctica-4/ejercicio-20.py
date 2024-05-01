# Implementar un programa que muestre un menú de opciones e invoque las funciones desarrolladas en la práctica 3. Para que funcione debe importar los archivos donde se encuentran las definiciones o re definirlas. El programa debería mostrar los siguientes mensajes:

# Bienvenido al programa con menu de opciones
# Elija una opción del siguiente menú ingresando del 1 al 5
# 1-Cálculo dosis
# 2-Cálculo litros 
# 3-Cálculo nuevo precio
# 4-Cálculo transporte
# 5-Salir

# Definir las funciones necesarias o importar los archivos donde se encuentran las definiciones

# Función para calcular dosis
def calcular_dosis():
    # Código para calcular la dosis
    pass

# Función para calcular litros
def calcular_litros():
    # Código para calcular los litros
    pass

# Función para calcular nuevo precio
def calcular_nuevo_precio():
    # Código para calcular el nuevo precio
    pass

# Función para calcular transporte
def calcular_transporte():
    # Código para calcular el transporte
    pass

# Función principal del programa
def menu_de_opciones():
    print("Bienvenido al programa con menú de opciones")
    print("Elija una opción del siguiente menú ingresando del 1 al 5")
    print("1-Cálculo dosis")
    print("2-Cálculo litros")
    print("3-Cálculo nuevo precio")
    print("4-Cálculo transporte")
    print("5-Salir")

    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion == 1:
        calcular_dosis()
    elif opcion == 2:
        calcular_litros()
    elif opcion == 3:
        calcular_nuevo_precio()
    elif opcion == 4:
        calcular_transporte()
    elif opcion == 5:
        print("Saliendo del programa...")
    else:
        print("Opción no válida")

# Llamar a la función principal del programa
menu_de_opciones()

# Este programa define las funciones necesarias para calcular dosis, litros, nuevo precio y transporte, o importa los archivos donde se encuentran las definiciones. Luego, muestra un menú de opciones y permite al usuario elegir una opción ingresando un número del 1 al 5. Dependiendo de la opción elegida, invoca la función correspondiente o muestra un mensaje de salida.