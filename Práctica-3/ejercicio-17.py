# Definir una función que reciba como  parámetro una lista de números y retornela suma del primer elemento con el último.

# Definición de la función sumaPrimUlt
def sumaPrimUlt(lis):
    suma = lis[0] + lis[-1]
    return suma

# Definición de la función promedioPrimUlt
def promedioPrimUlt(lis):
    promedio = (lis[0] + lis[-1]) / 2
    return promedio

# Programa principal
numeros = []  # Creamos una lista vacía para almacenar los números ingresados por el usuario

# Solicitamos al usuario 3 números y los agregamos a la lista
for i in range(3):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

# Invocamos las funciones y mostramos los resultados
resultado_suma = sumaPrimUlt(numeros)
resultado_promedio = promedioPrimUlt(numeros)

print("La suma del primer elemento con el último es: " + str(resultado_suma))
print("El promedio del primer elemento con el último es: " +str(resultado_promedio))

# En este código, definimos dos funciones: sumaPrimUlt y promedioPrimUlt. La función sumaPrimUlt recibe una lista de números y retorna la suma del primer elemento con el último elemento de la lista. La función promedioPrimUlt también recibe una lista de números y retorna el promedio del primer elemento con el último elemento de la lista.

# En el programa principal, solicitamos al usuario que ingrese 3 números y los agregamos a la lista numeros. Luego, invocamos las funciones sumaPrimUlt y promedioPrimUlt pasando la lista numeros como argumento y mostramos los resultados.