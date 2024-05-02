# Dada la siguiente lista [1, 14, 56, 43, 23, 46, 58, 123, 67 ] escribir una función que muestre el número más alto, escriba el programa que invoque a la función.

def encontrar_numero_mas_alto(lista):
    numero_mas_alto = max(lista)
    print("El número más alto es:", numero_mas_alto)

lista_numeros = [1, 14, 56, 43, 23, 46, 58, 123, 67]
encontrar_numero_mas_alto(lista_numeros)

# En esta función, utilizamos la función max para encontrar el número más alto de la lista dada. Luego, imprimimos ese número en pantalla.

# El programa principal crea una lista de números [1, 14, 56, 43, 23, 46, 58, 123, 67] y llama a la función encontrar_numero_mas_alto pasando esa lista como argumento.