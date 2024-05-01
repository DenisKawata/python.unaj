# Definir una función llamada CALCULO_LITROS que reciba tres números, el alto, ancho y profundidad (en metros) de unaa pileta y devuelva la cantidad de litros que tiene.

def calculo_litros(alto, ancho, profundidad):
    volumen = alto * ancho * profundidad * 1000

    return volumen   

# Ejemplo de uso de la función
alto = 2
ancho = 3
profundidad = 1.5

litros = calculo_litros(alto, ancho, profundidad)
print("La pileta tiene " + litros + " litros de agua.")

# En este código, la función CALCULO_LITROS recibe los parámetros alto, ancho y profundidad. Luego, se calcula el volumen de la pileta multiplicando estos valores y multiplicando por 1000 para convertir metros cúbicos a litros. Finalmente, se devuelve el volumen en litros.