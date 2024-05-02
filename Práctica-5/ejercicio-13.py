# Escriba un programa que solicite nombres de localidades y códigos postales al usuario hasta que se ingresa el código postal 0. Debe generar una lista con todos los valores ingresados e imprimirla. Utilice funciones para su resolución.

def solicitar_localidades_codigos_postales():
    localidades_codigos = []
    while True:
        localidad = input("Ingrese el nombre de una localidad: ")
        codigo_postal = int(input("Ingrese el código postal (0 para terminar): "))
        if codigo_postal == 0:
            break
        else:
            localidades_codigos.append((localidad, codigo_postal))
    return localidades_codigos

datos_localidades_codigos = solicitar_localidades_codigos_postales()
print("La lista de localidades y códigos postales ingresados es:")
print(datos_localidades_codigos)

# En este programa, la función solicitar_localidades_codigos_postales utiliza un bucle while True para solicitar al usuario que ingrese el nombre de una localidad y su código postal. En cada iteración, se lee la localidad y el código postal ingresados. Si el código postal es igual a 0, el bucle se interrumpe. Si no es igual a 0, se agrega una tupla con la localidad y el código postal a la lista localidades_codigos.

# Después de que el usuario termina de ingresar los datos, se imprime la lista datos_localidades_codigos que contiene todas las localidades y códigos postales ingresados.