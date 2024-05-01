# Dada la siguiente tabla: Transporte: Bicicleta, Moto, Auto, Camioneta, Colectivo, Avión, #Pasajeros: 1, 2, 4, 12, 40, 200. Escribir un programa que dada la cantidad de personas a vijar, recomiende el medio de transporte.

transporte = ["Bicicleta", "Moto", "Auto", "Camioneta", "Colectivo", "Avión"]
pasajeros = [1, 2, 4, 12, 40, 200]

cantidad_personas = int(input("Ingrese la cantidad de personas a viajar: "))

if cantidad_personas < 1:
    print("Ingrese una cantidad válida de personas.")
else:
    if cantidad_personas <= pasajeros[0]:
        print("Se recomienda utilizar la bicicleta.")
    elif cantidad_personas <= pasajeros[1]:
        print("Se recomienda utilizar la moto.")
    elif cantidad_personas <= pasajeros[2]:
        print("Se recomienda utilizar el auto.")
    elif cantidad_personas <= pasajeros[3]:
        print("Se recomienda utilizar la camioneta.")
    elif cantidad_personas <= pasajeros[4]:
        print("Se recomienda utilizar el colectivo.")
    else:
        print("Se recomienda utilizar el avión.")

# En este código, se define una lista llamada transporte que contiene los diferentes medios de transporte y otra lista llamada pasajeros que contiene la capacidad de cada medio de transporte. Luego, se lee la cantidad de personas a viajar utilizando la función input. A continuación, se utiliza una estructura condicional if-elif-else para determinar el medio de transporte recomendado según la cantidad de personas ingresadas. Si la cantidad de personas es menor o igual a la capacidad de un medio de transporte, se muestra el mensaje correspondiente recomendando ese medio de transporte. Si la cantidad de personas es mayor a la capacidad de todos los medios de transporte, se muestra el mensaje "Se recomienda utilizar el avión".