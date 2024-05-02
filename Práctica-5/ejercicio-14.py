# Realice un programa para manejar equipos de fútbol. 

# a) Definir una función que arme una lista con la información de los equipos. De cada equipo se quiere guardar el nombre del equipo, puntaje en la tabla de posiciones y la cantidad de goles a favor. El ingreso finaliza cuando se lee el nombre del equipo igual a ‘ZZZ’. 

def armar_lista_equipos():
    equipos = []
    while True:
        nombre_equipo = input("Ingrese el nombre del equipo ('ZZZ' para terminar): ")
        if nombre_equipo == 'ZZZ':
            break
        puntaje = int(input("Ingrese el puntaje en la tabla de posiciones: "))
        goles_a_favor = int(input("Ingrese la cantidad de goles a favor: "))
        equipos.append((nombre_equipo, puntaje, goles_a_favor))
    return equipos

lista_equipos = armar_lista_equipos()

# En esta función, utilizamos un bucle while True para solicitar al usuario que ingrese el nombre del equipo, el puntaje en la tabla de posiciones y la cantidad de goles a favor. En cada iteración, se lee la información ingresada. Si el nombre del equipo es igual a 'ZZZ', el bucle se interrumpe y se termina el ingreso de datos. Si no es igual a 'ZZZ', se agrega una tupla con la información del equipo a la lista equipos.

# b) Usando la lista anterior, escriba una funcion para imprimir la cantidad de goles a favor que tienen los equipos que están en la primera y última posición de la lista.

def imprimir_goles_primero_ultimo(lista_equipos):
    primer_equipo = lista_equipos[0]
    ultimo_equipo = lista_equipos[-1]
    goles_primer_equipo = primer_equipo[2]
    goles_ultimo_equipo = ultimo_equipo[2]
    print("Cantidad de goles a favor del primer equipo: " + str(goles_primer_equipo))
    print("Cantidad de goles a favor del último equipo: " + str(goles_ultimo_equipo))

imprimir_goles_primero_ultimo(lista_equipos)

# En esta función, utilizamos el índice [0] para obtener el primer equipo de la lista y el índice [-1] para obtener el último equipo de la lista. Luego, obtenemos la cantidad de goles a favor de cada equipo y los imprimimos en pantalla.

# c) escriba una funcion para imprimir el nombre del equipo Campeón de la lista del ejercicio anterior.

def imprimir_campeon(lista_equipos):
    equipo_campeon = max(lista_equipos, key=lambda x: x[1])
    nombre_campeon = equipo_campeon[0]
    print("El equipo campeón es: " + nombre_campeon)

imprimir_campeon(lista_equipos)

# En esta función, utilizamos la función max y la función lambda para encontrar el equipo con el puntaje más alto en la lista. Luego, obtenemos el nombre del equipo campeón y lo imprimimos en pantalla.