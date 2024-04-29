# Definir una función llamada CALCULO_REBAJA que reciba dos números, uno al precio anterior y otro para preccio rebajado y devuelva un número que represente el porcentaje rebajado.

def CALCULO_REBAJA(precio_anterior, precio_rebajado):
    porcentaje_rebajado = (precio_anterior - precio_rebajado) / precio_anterior * 100

    return porcentaje_rebajado

 # Ejemplo de uso de la función

precio_anterior = 100
precio_rebajado = 50
porcentaje_rebajado = CALCULO_REBAJA(precio_anterior, precio_rebajado)
print("El precio es: " + str(porcentaje_rebajado))

# En este código se define una función llamada CALCULO_REBAJA que recibe dos números, uno al precio anterior y otro para precio rebajado. Luego, devuelve un número que represente el porcentaje rebajado. 