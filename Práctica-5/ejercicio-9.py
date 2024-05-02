# Escriba un programa que solicite códigos postales de localidades e imprima si esa localidad es La Plata, Florencio Varela u otra. Recordar que el código postal de La Plata es 1900 y el de Florencia Varela es: 1887. El programa termina cuando se ingresa el código postal 0. Utilice funciones para su resolución.

def verificar_localidad(codigo_postal):
    if codigo_postal == 1900:
        return "La Plata"
    elif codigo_postal == 1887:
        return "Florencio Varela"
    else:
        return "Otra localidad"

def solicitar_codigos_postales():
    while True:
        codigo_postal = int(input("Ingrese un código postal (0 para terminar): "))
        if codigo_postal == 0:
            break
        else:
            localidad = verificar_localidad(codigo_postal)
            print(f"La localidad correspondiente al código postal {codigo_postal} es: {localidad}")

solicitar_codigos_postales()

# En este programa, la función verificar_localidad recibe un código postal como parámetro y verifica si es igual a 1900 (código postal de La Plata) o 1887 (código postal de Florencio Varela). Si es así, retorna el nombre de la localidad correspondiente. En caso contrario, retorna "Otra localidad".

# La función solicitar_codigos_postales utiliza un bucle while True para solicitar al usuario que ingrese códigos postales indefinidamente. En cada iteración, se lee el código postal ingresado. Si es igual a 0, el bucle se interrumpe y el programa termina. Si no es igual a 0, se llama a la función verificar_localidad para obtener la localidad correspondiente al código postal y se muestra en pantalla.