# Diseñar un programa que dado un número de 1 a 7 determine el día de la semana que representa: 1- Domingo a 7 - Sábado. ¿Qué pasa si ingreso un número mayor que 7?

numero = int(input("Ingrese un número del 1 al 7: "))

if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Lunes")
elif numero == 3:
    print("Martes")
elif numero == 4:
    print("Miércoles")
elif numero == 5:
    print("Jueves")
elif numero == 6:
    print("Viernes")
elif numero == 7:
    print("Sábado")
else:
    print("El número ingresado no es válido.")

# En este código, se utiliza la función input para solicitar a la persona usuaria que ingrese un número del 1 al 7. Luego, se utiliza una estructura condicional if-elif-else para determinar el día de la semana correspondiente al número ingresado. Si el número coincide con alguno de los casos, se muestra el día correspondiente. Si el número no coincide con ninguno de los casos (es mayor que 7), se muestra el mensaje "El número ingresado no es válido".