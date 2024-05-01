# A continuación se detallan las temperaturas máximas y mínimas de tres lugares de Argentina en un día del año:

# USHUAIA: MÁX: 13°C MÍN: -5°C

# BUENOS AIRES: MÁX: 16°C MÍN: 5°C

# BASE MARAMBIO: MÁX: 3°C MÍN: -20°C

# DEFINA UNA FUNCIÓN que reciba dos temperaturas y que muestre que indique la diferencia entre ambas.

# - Utilice la función anterior para mostrar la diferencia de temperaturas mínimas entre Buenos Aires y Ushuaia.
# - Utilice la función anterior para mostrar la diferencia de temperaturas mínimas entre Base Marambio y Ushuaia.
# - Utilice la función anterior para mostrar la diferencia de temperaturas máximas entre Buenos Aires y la mínima.
# - Si la temperatura máxima en Base Marambio bajó 7°C, que diferencia tendrá con la temperatura mínima.

# Si los datos ingresan por teclado, ¿qué cambios debe hace en su programa? Fundamente la respuesta.


def calcular_diferencia_temperaturas(temperatura1, temperatura2):
    diferencia = abs(temperatura1 - temperatura2)
    return diferencia

# Mostrar la diferencia de temperaturas mínimas entre Buenos Aires y Ushuaia
temperatura_buenos_aires_min = 5
temperatura_ushuaia_min = -5
diferencia_buenos_aires_ushuaia_min = calcular_diferencia_temperaturas(temperatura_buenos_aires_min, temperatura_ushuaia_min)
print("La diferencia de temperaturas mínimas entre Buenos Aires y Ushuaia es: " + str(diferencia_buenos_aires_ushuaia_min))

# Mostrar la diferencia de temperaturas mínimas entre Base Marambio y Ushuaia
temperatura_base_marambio_min = -20
diferencia_base_marambio_ushuaia_min = calcular_diferencia_temperaturas(temperatura_base_marambio_min, temperatura_ushuaia_min)
print("La diferencia de temperaturas mínimas entre Base Marambio y Ushuaia es: " + str(diferencia_base_marambio_ushuaia_min))

# Mostrar la diferencia de temperaturas máximas entre Buenos Aires y la mínima
temperatura_buenos_aires_max = 16
diferencia_buenos_aires_max_min = calcular_diferencia_temperaturas(temperatura_buenos_aires_max, temperatura_buenos_aires_min)
print("La diferencia de temperaturas máximas entre Buenos Aires y la mínima es: " + str(diferencia_buenos_aires_max_min))

# Calcular la diferencia de temperaturas en Base Marambio si la temperatura máxima bajó 7°C.
temperatura_base_marambio_max = 3
diferencia_base_marambio_max_min = calcular_diferencia_temperaturas(temperatura_base_marambio_max - 7, temperatura_base_marambio_min)
print("La diferencia de temperaturas en Base Marambio con la baja de 7°C en la temperatura máxima es: " + str(diferencia_base_marambio_max_min))

# En este código, se define una función llamada calcular_diferencia_temperaturas que recibe dos temperaturas como parámetros y retorna la diferencia absoluta entre ellas.


# Luego, se utilizan llamadas a esta función para calcular las diferencias de temperaturas solicitadas:

# 1- Se calcula la diferencia de temperaturas mínimas entre Buenos Aires y Ushuaia, utilizando las temperaturas mínimas de ambos lugares.
# 2- Se calcula la diferencia de temperaturas mínimas entre Base Marambio y Ushuaia, utilizando la temperatura mínima de Base Marambio y la temperatura mínima de Ushuaia.
# 3- Se calcula la diferencia de temperaturas máximas entre Buenos Aires y su temperatura mínima, utilizando la temperatura máxima de Buenos Aires y la temperatura mínima de Buenos Aires.
# 4- Se calcula la diferencia de temperaturas en Base Marambio si la temperatura máxima bajó 7°C, utilizando la temperatura máxima actualizada de Base Marambio y la temperatura mínima de Base Marambio.


# Si los datos ingresan por teclado, deberás modificar el código para solicitar las temperaturas al usuario utilizando la función input. Por ejemplo:

temperatura_buenos_aires_min = float(input("Ingrese la temperatura mínima de Buenos Aires: "))
temperatura_ushuaia_min = float(input("Ingrese la temperatura mínima de Ushuaia: "))

# De esta manera, el usuario podrá ingresar las temperaturas al ejecutar el programa.