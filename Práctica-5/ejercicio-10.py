# Definir una función que imprima los primeros cien números enteros. ¿Se le ocurre otra forma de hacerlo?

def imprimir_primeros_cien_numeros():
    for numero in range(1, 101):
        print(numero)

imprimir_primeros_cien_numeros()

# En esta función, utilizamos un bucle for para iterar desde 1 hasta 100 (inclusive) utilizando la función range. En cada iteración, se imprime el número correspondiente.

# Otra forma de hacerlo sería utilizando un bucle while:

def imprimir_primeros_cien_numeros():
    numero = 1
    while numero <= 100:
        print(numero)
        numero += 1

imprimir_primeros_cien_numeros()

# En este caso, utilizamos un bucle while que se ejecuta mientras el número sea menor o igual a 100. En cada iteración, se imprime el número y se incrementa en 1.

# Ambas formas son válidas y producirán el mismo resultado: imprimir los primeros cien números enteros.