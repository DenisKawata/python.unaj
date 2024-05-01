# Dada la siguiente tabla: Categoria : A, B, C. Antiguedad: [< 10 años, entre 10 a 15, >15], [< 10 años, entre 10 a 15, >15], [< 10 años, entre 10 a 15, >15]. Aumento: [5 %, 10 %, 15 %], [10 %, 15 %, 20 %], [15 %, 20 %, 25 %]. Escriba un programa que solicite a una person su nombre, apellido, sueldo básico, categoria y antiguedad. El programa le debe calcular el aumento de acuerdo a la tabla y mostrarle el sueldo anterior, el aumento y el sueldo actualizado con dicho aumento. RESUELVA UTILIZANDO FUNCIONES.

def calcular_aumento(sueldo_basico, categoria, antiguedad):
    tabla_categoria = ["A", "B", "C"]
    tabla_antiguedad = ["< 10 años", "entre 10 a 15", "> 15"]
    tabla_aumento = [
        [5, 10, 15],
        [10, 15, 20],
        [15, 20, 25]
    ]

    indice_categoria = tabla_categoria.index(categoria)
    indice_antiguedad = tabla_antiguedad.index(antiguedad)
    aumento = tabla_aumento[indice_categoria][indice_antiguedad]

    sueldo_anterior = sueldo_basico
    sueldo_actualizado = sueldo_basico + (sueldo_basico * aumento / 100)

    return sueldo_anterior, aumento, sueldo_actualizado

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
sueldo_basico = float(input("Ingrese su sueldo básico: "))
categoria = input("Ingrese su categoría (A, B o C): ")
antiguedad = input("Ingrese su antigüedad (< 10 años, entre 10 a 15, > 15): ")

sueldo_anterior, aumento, sueldo_actualizado = calcular_aumento(sueldo_basico, categoria, antiguedad)

print("Nombre: " + nombre)
print("Apellido: " + apellido)
print("Sueldo anterior: " + str(sueldo_anterior))
print("Aumento: " + str(aumento) + "%")
print("Sueldo actualizado:" + str(sueldo_actualizado))

# En este código, se define una función llamada calcular_aumento que recibe el sueldo básico, la categoría y la antigüedad de una persona. Dentro de la función, se utiliza una tabla para determinar el aumento correspondiente según la categoría y la antigüedad ingresadas. Luego, se calcula el sueldo anterior, el aumento y el sueldo actualizado.

# Después, se solicita a la persona usuaria que ingrese su nombre, apellido, sueldo básico, categoría y antigüedad. Se llama a la función calcular_aumento con los valores ingresados y se almacenan los resultados en variables. Finalmente, se muestra en pantalla el nombre, apellido, sueldo anterior, aumento y sueldo actualizado.