# Dado la duración (en segundos) de una llamada telefónica, calcular su costo, de la siguiente manera: El primer minutos $1,10, luego $0,25 cada fracción de 15 segundos (un cuarto de minuto).

def calcular_costo_llamada(duracion):
    minutos = duracion // 60
    segundos_restantes = duracion % 60

    costo = 1.10  # Costo del primer minuto
    if minutos > 0:
        costo += (minutos - 1) * 0.25  # Costo de los minutos adicionales

    # Calcular el costo de los segundos restantes (fracción de 15 segundos)
    costo += (segundos_restantes // 15) * 0.25

    return costo

duracion_llamada = int(input("Ingrese la duración de la llamada en segundos: "))

costo_llamada = calcular_costo_llamada(duracion_llamada)

print("El costo de la llamada es: " + str(costo_llamada))

# En este código, se define una función llamada calcular_costo_llamada que recibe la duración de la llamada en segundos como parámetro. Dentro de la función, se divide la duración en minutos y segundos restantes. Luego, se establece el costo inicial de $1.10 para el primer minuto de la llamada. Si la duración es mayor a 1 minuto, se calcula el costo de los minutos adicionales, sumando $0.25 por cada minuto adicional.

# Después, se calcula el costo de los segundos restantes, dividiendo la cantidad de segundos por 15 y multiplicando por $0.25 (el costo de cada fracción de 15 segundos).

# Finalmente, se muestra en pantalla el costo total de la llamada.