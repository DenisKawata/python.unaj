# Escribir un programa que muestre la tabla de los códigos ASCII. Los códigos ASCII van de 0 a 255

def tabla_ascii():
    for i in range(256):
        print(f"Carácter: {chr(i)} - Código ASCII: {i}")

tabla_ascii()

# En este programa, la función tabla_ascii utiliza un bucle for para iterar a través de los números del 0 al 255. En cada iteración, se imprime el carácter correspondiente al código ASCII actual utilizando la función chr y se muestra el código ASCII.