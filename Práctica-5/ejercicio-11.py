# Implementar una función que muestre todos los múltiplos de n entre n y m · n, ambos inclusive, donde n y m son parámetros de la función.

def mostrar_multiplos(n, m):
    for numero in range(n, (m * n) + 1, n):
        print(numero)

mostrar_multiplos(3, 5)

# En esta función, utilizamos un bucle for y la función range para iterar desde n hasta m * n, incrementando en n en cada iteración. Esto nos permite obtener todos los múltiplos de n en ese rango. En cada iteración, imprimimos el número correspondiente.

# Por ejemplo, si llamamos a la función mostrar_multiplos(3, 5), nos mostrará todos los múltiplos de 3 entre 3 y 15 (ambos inclusive), que son 3, 6, 9, 12 y 15.