# Definir una función llamada PRECIO_CON_IVA que agrega el IVA (21%) de un producto dado su precio de venta sin IVA.

def precio_con_iva(precio_sin_iva):
    iva = 0.21  # Porcentaje de IVA (21%)
    precio_con_iva = precio_sin_iva * (1 + iva)
    return precio_con_iva

# En este ejemplo, la función precio_con_iva recibe el parámetro precio_sin_iva, que representa el precio de venta sin IVA. Luego, se calcula el precio con IVA multiplicando el precio sin IVA por 1 más el porcentaje de IVA. Finalmente, se devuelve el precio con IVA.