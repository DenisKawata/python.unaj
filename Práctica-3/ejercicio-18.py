# En este código una fracción está representada por una lista de dos elemtos, el numerador y el denominador. Por ejemplo la fracción 3/4 seria la lista (3,4). Complete el código según corresponda.

# Zona de definiciones de funciones
def cargarFraccion():
    numerador = int(input("Ingrese el numerador: "))
    denominador = int(input("Ingrese el denominador: "))
    fraccion = [numerador, denominador]
    return fraccion

def numeradorFraccion(x):
    return x[0]

def denominadorFraccion(x):
    return x[1]

def sumaFracciones(x, y):
    numerador = x[0] * y[1] + y[0] * x[1]
    denominador = x[1] * y[1]
    return [numerador, denominador]

def restaFracciones(x, y):
    numerador = x[0] * y[1] - y[0] * x[1]
    denominador = x[1] * y[1]
    return [numerador, denominador]

def divisionFracciones(x, y):
    numerador = x[0] * y[1]
    denominador = x[1] * y[0]
    return [numerador, denominador]

def multiplicacionFracciones(x, y):
    numerador = x[0] * y[0]
    denominador = x[1] * y[1]
    return [numerador, denominador]

# Zona del programa principal
print("Bienvenidos/as a cuentas con Fracciones")
a = cargarFraccion()
b = cargarFraccion()

print("El denominador de la primera fracción es: " + str(denominadorFraccion(a)))
print("El numerador de la segunda fracción es: " + str(numeradorFraccion(b)))

suma = sumaFracciones(a, b)
resta = restaFracciones(a, b)
multiplicacion = multiplicacionFracciones(a, b)
division = divisionFracciones(a, b)

print("La suma de dichas fracciones es: " + str(suma))
print("La resta de dichas fracciones es: " + str(resta))
print("La multiplicación de dichas fracciones es: " + str(multiplicacion))
print("La división es: " + str(division))

# En este código, definimos las funciones solicitadas. La función cargarFraccion solicita al usuario el numerador y el denominador, arma la fracción como una lista y la retorna. Las funciones numeradorFraccion y denominadorFraccion retornan el numerador y el denominador de la fracción, respectivamente. Las funciones sumaFracciones, restaFracciones, multiplicacionFracciones y divisionFracciones realizan las operaciones matemáticas correspondientes con las fracciones representadas como listas.

# En el programa principal, solicitamos al usuario que ingrese los numeradores y denominadores para las fracciones a y b, luego mostramos el denominador de la primera fracción, el numerador de la segunda fracción y los resultados de las operaciones de suma, resta, multiplicación y división entre las fracciones.