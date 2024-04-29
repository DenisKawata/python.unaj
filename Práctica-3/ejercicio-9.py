# Definir una función llamada CALCULO_NUEVO_PRECIO que reciba dos números, uno con el precio anterior y otro con el número de porcentaje a aumentar y devuelva el precio aumentado.

def calculo_nuevo_precio(precio_anterior, porcentaje_aumento):
    precio_aumentado = precio_anterior + (precio_anterior * porcentaje_aumento / 100)

    return precio_aumentado

 # Ejemplo de uso de la función
precio_anterior = 100
porcentaje_aumento = 10

precio_aumentado = calculo_nuevo_precio(precio_anterior, porcentaje_aumento)

print("El nuevo precio es: " + str (precio_aumentado))

# En este código, la función CALCULO_NUEVO_PRECIO recibe dos parámetros, precio_anterior y porcentaje_aumento. Luego, calcula el nuevo precio del producto, sumando el precio anterior al precio anterior multiplicado por el porcentaje de aumento dividido entre 100. Finalmente, devuelve el nuevo precio.
