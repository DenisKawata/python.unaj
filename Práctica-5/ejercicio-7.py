# Escriba un programa y las funciones necesarias para leer números de documentos de identidad de personas hasta que se ingrese el número “999”. Debe imprimir la cantidad de números de documentos menores que 20.000.000.

def contar_documentos_menores():
    contador = 0
    while True:
        documento = int(input("Ingrese un número de documento ('999' para terminar): "))
        if documento == 999:
            break
        elif documento < 20000000:
            contador += 1
    return contador

cantidad_documentos_menores = contar_documentos_menores()
print("La cantidad de números de documentos menores que 20.000.000 es: " + str(cantidad_documentos_menores))

# En este programa, la función contar_documentos_menores utiliza un bucle while True para leer números de documentos de identidad indefinidamente. En cada iteración, se solicita al usuario que ingrese un número de documento. Si el número ingresado es "999", el bucle se interrumpe y el programa termina. Si el número ingresado es menor que 20.000.000, se incrementa el contador en 1.

# En el programa principal, se llama a la función contar_documentos_menores y se guarda el resultado en la variable cantidad_documentos_menores. Luego, se muestra la cantidad de números de documentos menores que 20.000.000.