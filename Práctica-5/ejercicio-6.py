# Escriba un programa y las funciones necesarias para leer nombres de personas hasta que se ingrese el nombre “zzz”. Debe imprimir la cantidad de nombres que comienzan con “A”.

def contar_nombres_con_a():
    contador = 0
    while True:
        nombre = input("Ingrese un nombre ('zzz' para terminar): ")
        if nombre == "zzz":
            break
        elif nombre[0].lower() == "a":
            contador += 1
    return contador

cantidad_nombres_con_a = contar_nombres_con_a()
print("La cantidad de nombres que comienzan con 'A' es: " + str(cantidad_nombres_con_a))

# En este programa, la función contar_nombres_con_a utiliza un bucle while True para leer nombres de personas indefinidamente. En cada iteración, se solicita al usuario que ingrese un nombre. Si el nombre ingresado es "zzz", el bucle se interrumpe y el programa termina. Si el nombre ingresado no es "zzz", se verifica si el primer carácter del nombre (convertido a minúscula) es igual a "a". Si es así, se incrementa el contador en 1.

# En el programa principal, se llama a la función contar_nombres_con_a y se guarda el resultado en la variable cantidad_nombres_con_a. Luego, se muestra la cantidad de nombres que comienzan con "A".