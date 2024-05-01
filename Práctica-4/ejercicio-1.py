# Escribir un programa que lee un número ingresado por la persona usuaria en pantalla y muestre si es positivo, negativo o cero.

numero = float(input("Ingrese un número: "))

if numero > 0:
    print("El número ingresado es positivo.")
elif numero < 0:
    print("El número ingresado es negativo.")
else:
    print("El número ingresado es cero.")

# En este código, se utiliza la función input para solicitar a la persona usuaria que ingrese un número. Luego, se utiliza la estructura condicional if-elif-else para determinar si el número es positivo, negativo o cero. Si el número es mayor que cero, se muestra el mensaje "El número ingresado es positivo". Si el número es menor que cero, se muestra el mensaje "El número ingresado es negativo". Si el número es igual a cero, se muestra el mensaje "El número ingresado es cero".