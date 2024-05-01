# Diseña un programa que, dado un número entero, determine si  éste es el doble de un número impar. (Ejemplo: 14 es el doble de 7, que es impar.) RESUELVA UTILIZANDO FUNCIONES

def es_doble_de_impar(numero):
    if numero % 2 == 0:
        mitad = numero // 2
        if mitad % 2 != 0:
            return True
    return False

numero = int(input("Ingrese un número entero: "))

if es_doble_de_impar(numero):
    print("El número" + str(numero) + "es el doble de un número impar.")
else:
    print("El número" + str(numero) + "no es el doble de un número impar.")

# En este código, se define una función llamada es_doble_de_impar que recibe un número entero como parámetro. Dentro de la función, se verifica si el número es par utilizando el operador % para obtener el resto de la división por 2. Si el número es par, se divide por 2 y se verifica si la mitad es impar. Si la mitad es impar, se retorna True, indicando que el número es el doble de un número impar. En caso contrario, se retorna False.

# Después, se solicita a la persona usuaria que ingrese un número entero. Se llama a la función es_doble_de_impar con el número ingresado y se verifica si es el doble de un número impar. Finalmente, se muestra en pantalla si el número es o no el doble de un número impar.