# Diseñar un programa que dado un cáracter imprima en pantalla sí es una letra, un dígito, un carácter especial u otro tipo de cáracter.

def tipo_caracter(caracter):
    if caracter.isalpha():
        return "letra"
    elif caracter.isdigit():
        return "dígito"
    elif not (caracter.isspace() or caracter.isalnum()):
        return "carácter especial"
    else:
        return "otro tipo de carácter"

caracter = input("Ingrese un carácter: ")

tipo = tipo_caracter(caracter)

print(f"El carácter '{caracter}' es un(a) {tipo}.")

# En este código, se define una función llamada tipo_caracter que recibe un carácter como parámetro. Dentro de la función, se utilizan los métodos de cadenas de Python para verificar si el carácter es una letra, un dígito, un carácter especial o algún otro tipo de carácter. Dependiendo del resultado de estas verificaciones, se retorna el tipo correspondiente.

# Después, se solicita a la persona usuaria que ingrese un carácter. Se llama a la función tipo_caracter con el carácter ingresado y se determina su tipo. Finalmente, se muestra en pantalla el tipo de carácter al que pertenece el carácter ingresado.