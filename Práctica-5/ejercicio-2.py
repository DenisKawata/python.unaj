# Escribir un programa y su respectiva función que calcule la sumatoria desde 0 hasta m, donde m es un número introducido por la persona usuaria desde el teclado.

def calcular_sumatoria(numero):
    sumatoria = 0
    for i in range(numero + 1):
        sumatoria += i
    return sumatoria

numero = int(input("Ingrese un número: "))
resultado = calcular_sumatoria(numero)
print("La sumatoria desde 0 hasta " + str(numero) + " es: " + str(resultado))

# En este programa, la función calcular_sumatoria recibe un número como parámetro y utiliza un bucle for para iterar desde 0 hasta ese número. En cada iteración, se suma el valor actual a la variable sumatoria. Al finalizar el bucle, se retorna el valor de sumatoria.

# En el programa principal, se solicita al usuario que ingrese un número y se llama a la función calcular_sumatoria con ese número. Luego, se muestra el resultado de la sumatoria.