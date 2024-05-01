#  Desarrollar un programa en el que se ingrese el año de nacimiento de una persona e indique si la persona de bebé, menor, adoleccente, adulto o adulto mayor. Usando la siguiente tabla: Tipo: Bebé, Menor, Adolecente, Adulto, Adulto mayor. Edad: < 2 años, > 2 y <=12, >12 y <=18, >18 y <=60, >60.

anio_nacimiento = int(input("Ingrese el año de nacimiento: "))
edad = 2024 - anio_nacimiento

if edad < 2:
    print("La persona es un bebé.")
elif edad <= 12:
    print("La persona es un menor.")
elif edad <= 18:
    print("La persona es un adolescente.")
elif edad <= 60:
    print("La persona es un adulto.")
else:
    print("La persona es un adulto mayor.")

# En este código, se lee el año de nacimiento de una persona utilizando la función input. Luego, se calcula la edad de la persona restando el año de nacimiento del año actual (2024). A continuación, se utiliza una estructura condicional if-elif-else para determinar la categoría de la persona según su edad. Si la edad es menor a 2 años, se muestra el mensaje "La persona es un bebé". Si la edad está entre 2 y 12 años, se muestra "La persona es un menor". Si la edad está entre 13 y 18 años, se muestra "La persona es un adolescente". Si la edad está entre 19 y 60 años, se muestra "La persona es un adulto". Si la edad es mayor a 60 años, se muestra "La persona es un adulto mayor".