# Escribir un programa y las funciones necesarias para resolver que se lean letras del teclado indefinidamente hasta que el usuario ingrese “fin” e imprima el código ASCII de las mismas.

def leer_letras():
    while True:
        letra = input("Ingrese una letra ('fin' para terminar): ")
        if letra == "fin":
            break
        else:
            codigo_ascii = ord(letra)
            print(f"La letra '{letra}' tiene el código ASCII: {codigo_ascii}")

leer_letras()

# En este programa, la función leer_letras utiliza un bucle while True para leer letras del teclado indefinidamente. En cada iteración, se solicita al usuario que ingrese una letra. Si la letra ingresada es "fin", el bucle se interrumpe y el programa termina. Si la letra ingresada no es "fin", se utiliza la función ord para obtener el código ASCII de la letra y se imprime en pantalla.