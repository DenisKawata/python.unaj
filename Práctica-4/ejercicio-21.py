# Analizar el siguiente programa y completar el codigo que falta.

# Zona de definición de funciones

#def cargarDatos():
    # pide nombre, apellido, edad y sueldo a una persona, arma una lista y la retorna
#    ...
#def esMayorDeEdad(pers):
    # retorna verdadero True si es mayor a 18 años, sino retorna falso False
#    ...
#def personaMejorSueldo(pers1, pers2):
    # retorna el nombre y apellido de la persona que gana mas
#    ...
#def personaMasJoven(pers1, pers2):
    # retorna el nombre y apellido de la persona más joven de edad
#    ...    

# Zona del programa principal
#print ("Bienvenidos/as al programa sobre datos de personas")
#print("Se solicitara datos de 2 personas y se mostrara informacion de ellas")
# Utilizar la función para cargar datos de dos personas
#...
#...
#print("La persona que gana es: ", ......................)
#print("La persona mas chica es: ", .....................)
# Imprimir si la persona mayor es la que más gana o sea que mayor sueldo tiene.
#...


# Zona de definición de funciones

def cargarDatos():
    # pide nombre, apellido, edad y sueldo a una persona, arma una lista y la retorna
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))
    sueldo = float(input("Ingrese el sueldo: "))
    return [nombre, apellido, edad, sueldo]

def esMayorDeEdad(pers):
    # retorna verdadero True si es mayor a 18 años, sino retorna falso False
    return pers[2] > 18

def personaMejorSueldo(pers1, pers2):
    # retorna el nombre y apellido de la persona que gana mas
    if pers1[3] > pers2[3]:
        return pers1[0], pers1[1]
    else:
        return pers2[0], pers2[1]

def personaMasJoven(pers1, pers2):
    # retorna el nombre y apellido de la persona más joven de edad
    if pers1[2] < pers2[2]:
        return pers1[0], pers1[1]
    else:
        return pers2[0], pers2[1]

# Zona del programa principal
print("Bienvenidos/as al programa sobre datos de personas")
print("Se solicitarán datos de 2 personas y se mostrará información de ellas")

# Utilizar la función para cargar datos de dos personas
persona1 = cargarDatos()
persona2 = cargarDatos()

# Mostrar la persona que gana más y la persona más joven
print("La persona que gana es: ", personaMejorSueldo(persona1, persona2))
print("La persona más joven es: ", personaMasJoven(persona1, persona2))

# Imprimir si la persona mayor es la que más gana o sea que mayor sueldo tiene.
if personaMejorSueldo(persona1, persona2)[0] == personaMasJoven(persona1, persona2)[0]:
    print("La persona mayor es la que más gana.")
else:
    print("La persona mayor no es la que más gana.")

# En este programa, se completaron las funciones cargarDatos, esMayorDeEdad, personaMejorSueldo y personaMasJoven para realizar las tareas requeridas. Luego, en la zona del programa principal, se utilizan estas funciones para cargar los datos de dos personas, mostrar la persona que gana más, la persona más joven y determinar si la persona mayor es la que más gana.

