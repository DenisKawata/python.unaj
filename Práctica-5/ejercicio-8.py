# Escriba un programa y las funciones necesarias para recibir del usuario su nombre, apellido y patente hasta que ingrese AAA, e imprima si está exento de impuesto o no. Tener en cuenta que los autos cuyas patentes empiezan con R, S y T no deben pagar impuesto.

def verificar_impuesto():
    while True:
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        patente = input("Ingrese su patente ('AAA' para terminar): ")
        if patente == "AAA":
            break
        elif patente[0].upper() in ['R', 'S', 'T']:
            print(f"El vehículo con patente {patente} está exento de impuesto.")
        else:
            print(f"El vehículo con patente {patente} no está exento de impuesto.")

verificar_impuesto()

# En este programa, la función verificar_impuesto utiliza un bucle while True para recibir del usuario su nombre, apellido y patente indefinidamente. En cada iteración, se solicita al usuario que ingrese su nombre, apellido y patente. Si la patente ingresada es "AAA", el bucle se interrumpe y el programa termina. Si la patente ingresada comienza con R, S o T, se muestra un mensaje indicando que el vehículo está exento de impuesto. En caso contrario, se muestra un mensaje indicando que el vehículo no está exento de impuesto.