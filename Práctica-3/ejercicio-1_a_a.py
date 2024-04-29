# A) Dado el siguiente código indique cuáles son los parámetros reales y los formales:
    # a) Definición de funciones
def sumaAlcuadrado(x, y):
    rta= x**2 + 2*x*y + y**2
    return rta

 # Programa principal
print("Bienvenidos/as a la Suma al Cuadrado")
a = input("Ingrese el valor de a: ") 
b = input("Ingrese el valor de b: ")
print(sumaAlcuadrado(a, b))

    # En el código proporcionado, los parámetros reales son los valores ingresados por el usuario, mientras que los parámetros formales son los valores que se pasan a la función.

