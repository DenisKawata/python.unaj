# Escribir un programa que indique si un númeroes divisible por 6. ¿Cómo lo modificaría si se pidde lo mismo pero que voque una función definida por Ud.? Esta función debe llamare ES_DIVISIBLE y debe recibir dos parámetros "n" y "m" y retorna True si m es divisible por n sino retorna False.

# Programa sin función personalizada
numero = int(input("Ingrese un número: "))

if numero % 6 == 0:
    print("El número es divisible por 6.")
else:
    print("El número no es divisible por 6.")

# Programa con función personalizada ES_DIVISIBLE
def es_divisible(n, m):
    if m % n == 0:
        return True
    else:
        return False

numero = int(input("Ingrese un número: "))

if es_divisible(6, numero):
    print("El número es divisible por 6.")
else:
    print("El número no es divisible por 6.")

# En el primer bloque de código, se lee un número ingresado por la persona usuaria y se verifica si es divisible por 6 utilizando el operador de módulo (%). Si el resto de la división es igual a 0, se muestra el mensaje "El número es divisible por 6". De lo contrario, se muestra el mensaje "El número no es divisible por 6".

# En el segundo bloque de código, se define una función personalizada llamada ES_DIVISIBLE que recibe dos parámetros: n y m. La función verifica si m es divisible por n utilizando el operador de módulo y retorna True si lo es, y False en caso contrario. Luego, se lee un número ingresado por la persona usuaria y se utiliza la función ES_DIVISIBLE para determinar si es divisible por 6. El resultado se muestra en pantalla de acuerdo al resultado obtenido.