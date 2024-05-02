# Escribir un programa y su respectiva función que muestre la tabla de multiplicar de un número introducido por teclado por el usuario.

def tabla_de_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_de_multiplicar(numero)

# En este programa, la función tabla_de_multiplicar recibe un número como parámetro y luego utiliza un bucle for para imprimir la tabla de multiplicar de ese número, desde 1 hasta 10. Luego, en el programa principal, se solicita al usuario que ingrese un número y se llama a la función tabla_de_multiplicar con el número ingresado.