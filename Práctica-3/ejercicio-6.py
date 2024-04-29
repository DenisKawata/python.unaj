# definir una función ue reciba un número como parámetro y mostrar la tabla de multiplcar de dicho número.
def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = numero * i
        print(numero + " x " + i + " = " + resultado)

tabla_multiplicar(5)

# En este código, la función TABLA_MULTIPLICAR utiliza un bucle for para iterar de 1 hasta 10 veces. En cada iteración, se calcula el producto del número ingresado por el usuario y el número de iteración actual. El resultado se imprime en la pantalla. La función TABLA_MULTIPLICAR se llama en la línea 7, donde se pasa el número 5 como parámetro. Esto hace que se ejecute el bucle for y se imprima la tabla de multiplicar del número 5.