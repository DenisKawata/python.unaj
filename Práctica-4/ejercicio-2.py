# Escribir un programa que lee el nombre y apellido de una persona y muestra en pantalla si tiene la misma inicial o no.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

if nombre[0].lower() == apellido[0].lower():
    print("El nombre y el apellido tienen la misma inicial.")
else:
    print("El nombre y el apellido no tienen la misma inicial.")

# En este código, utilizamos la función input para solicitar a la persona usuaria que ingrese su nombre y apellido. Luego, utilizamos una estructura condicional if para comparar la primera letra del nombre (nombre[0]) con la primera letra del apellido (apellido[0]). Utilizamos el método lower() para convertir ambas letras a minúsculas y así evitar problemas de comparación por mayúsculas y minúsculas. Si las iniciales son iguales, se muestra el mensaje "El nombre y el apellido tienen la misma inicial". De lo contrario, se muestra el mensaje "El nombre y el apellido no tienen la misma inicial".