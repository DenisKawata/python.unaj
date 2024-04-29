# Definir una función llamada CALCULO_TRANSPORTE que reciba cuatro numeros: la cantidad de alumnos 1era, 2da y 3er. Salita de un jardin de infantes y la cantidad de asientos del transporte escolar. Lafunción debe retornar cuánto micros necesito contratar para una excursión sabiendo  que cada salita es acompañada por tres adultos.

def calculo_transporte(alumnos_1ra_sala, alumnos_2da_sala, alumnos_3ra_sala, asientos_transporte):
    adultos_1ra_sala = alumnos_1ra_sala // 3
    adultos_2da_sala = alumnos_2da_sala // 3
    adultos_3ra_sala = alumnos_3ra_sala // 3
    
    total_alumnos = alumnos_1ra_sala + alumnos_2da_sala + alumnos_3ra_sala
    total_adultos = adultos_1ra_sala + adultos_2da_sala + adultos_3ra_sala
    
    micros_necesarios = (total_alumnos + total_adultos) // asientos_transporte
    
    return micros_necesarios

# Ejemplo de uso de la función
alumnos_1ra_sala = 20
alumnos_2da_sala = 15
alumnos_3ra_sala = 18
asientos_transporte = 50

micros_necesarios = calculo_transporte(alumnos_1ra_sala, alumnos_2da_sala, alumnos_3ra_sala, asientos_transporte)
print("Se necesitan contratar" + micros_necesarios + "micros para la excursión.")

# En este código, la función CALCULO_TRANSPORTE recibe como parámetros los valores de los alumnos de cada sala y la cantidad de asientos del transporte escolar. Luego, calcula la cantidad de adultos que hay en cada sala y la cantidad total de alumnos y adultos. Finalmente, calcula la cantidad de micros necesarios para la excursión. 