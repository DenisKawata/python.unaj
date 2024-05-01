# DEFINA UNA FUNCIÓN que reciba un carácter cualquiera desde el teclado, y muestre el mensaje @Es una MAYÚSCULA Cuando el carácter sea una letra mayúscula u @Es una MINÚSCULA cuando sea una minúscula. En cualquier otro caso, no  mostrará mensaje alguno. (Considera únicamente letras del alfabeto)
# Pista: aunque parexca una obviedad, recuerda que letra es minúscula si está entre la 'a' y la 'z', y mayúscula si está entre la 'A' y la 'Z', también debe hacer la correspondiente invocación.
 
def determinar_tipo_caracter(caracter):
    if caracter.isupper():
        return "mayúscula"
    elif caracter.islower():
        return "minúscula"
    else:
        return None

caracter = input("Ingrese un carácter: ")

tipo = determinar_tipo_caracter(caracter)

if tipo == "mayúscula":
    print("Es una MAYÚSCULA.")
elif tipo == "minúscula":
    print("Es una MINÚSCULA.")

# En este código, se define una función llamada determinar_tipo_caracter que recibe un carácter como parámetro. Dentro de la función, se utilizan los métodos isupper() y islower() para verificar si el carácter es una letra mayúscula o minúscula, respectivamente. Si el carácter es una letra mayúscula, se retorna el valor "mayúscula". Si el carácter es una letra minúscula, se retorna el valor "minúscula". En cualquier otro caso, se retorna None.

# Después, se solicita a la persona usuaria que ingrese un carácter. Se llama a la función determinar_tipo_caracter con el carácter ingresado y se determina si es una letra mayúscula o minúscula. Si es una letra mayúscula, se muestra el mensaje "Es una MAYÚSCULA.". Si es una letra minúscula, se muestra el mensaje "Es una MINÚSCULA.".

