# Definir una función llamada CALCULO_DOSIS que recibe tres números. Uno para la cantidad de días que debe suministrarse el remedio, el segundo dato para la cantidad de veces por día que debe tomarlo, y el último dato para la cantidad de comprimidos que trae el envase. La función debe devolver verdadero si el envase alcanza para ese tratamiento y falso si no alcanza.

def calculo_dosis(cantidad_dias, veces_por_dia, comprimidos_envase):
    dosis_necesaria = cantidad_dias * veces_por_dia
    if dosis_necesaria <= comprimidos_envase:
        return True
    else:
        return False

# Ejemplo de uso de la función
cantidad_dias = 10
veces_por_dia = 3
comprimidos_envase = 50

envase_suficiente = calculo_dosis(cantidad_dias, veces_por_dia, comprimidos_envase)
if envase_suficiente:
    print("El envase alcanza para el tratamiento.")
else:
    print("El envase no alcanza para el tratamiento.")

# En este código, la función calculo_dosis recibe los parámetros cantidad_dias, veces_por_dia y comprimidos_envase. Luego, se calcula la dosis necesaria multiplicando la cantidad de días por la cantidad de veces por día que debe tomarse el remedio. Después, se compara la dosis necesaria con la cantidad de comprimidos que trae el envase. Si la dosis necesaria es menor o igual a la cantidad de comprimidos, la función devuelve True. De lo contrario, devuelve False.