# Dadas 3 longitudes, decir mediante un mensaje si se forma o no un triángulo (cada lado tiene que ser menor que la suma de los otros dos)

def es_triangulo(lado1, lado2, lado3):
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        return True
    else:
        return False

longitud1 = float(input("Ingrese la longitud del primer lado: "))
longitud2 = float(input("Ingrese la longitud del segundo lado: "))
longitud3 = float(input("Ingrese la longitud del tercer lado: "))

if es_triangulo(longitud1, longitud2, longitud3):
    print("Se puede formar un triángulo con las longitudes ingresadas.")
else:
    print("No se puede formar un triángulo con las longitudes ingresadas.")

# En este código, se define una función llamada es_triangulo que recibe tres longitudes como parámetros. Dentro de la función, se verifica si se cumple la condición para formar un triángulo: cada longitud debe ser menor que la suma de las otras dos longitudes. Si se cumple esta condición, se retorna True, indicando que se puede formar un triángulo. En caso contrario, se retorna False.

# Después, se solicita a la persona usuaria que ingrese las tres longitudes de los lados. Se llama a la función es_triangulo con las longitudes ingresadas y se verifica si se puede formar un triángulo. Finalmente, se muestra en pantalla si se puede o no formar un triángulo con las longitudes ingresadas.