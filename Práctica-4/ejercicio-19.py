# Una persona compró 4 kilogramos de vacío en esta carnicería y por pago en efectivo le hicieron un descuento del 5%, ¿cuánto dinero gastó?

# DEFINIR UNA FUNCIÓN que reciba dos números, que representan el porcentaje de descuento y el monto total, y retorne el monto con el descuento aplicado.

def calcular_monto_con_descuento(porcentaje_descuento, monto_total):
    descuento = (porcentaje_descuento / 100) * monto_total
    monto_con_descuento = monto_total - descuento
    return monto_con_descuento

porcentaje_descuento = 5
monto_total = 4 * 1044.90  # Multiplicamos el precio por kilogramo por la cantidad de kilogramos

monto_con_descuento = calcular_monto_con_descuento(porcentaje_descuento, monto_total)

print("La persona gastó: " + str(monto_con_descuento) + " pesos")

# En este código, se define una función llamada calcular_monto_con_descuento que recibe dos números como parámetros: el porcentaje de descuento y el monto total. Dentro de la función, se calcula el descuento multiplicando el porcentaje de descuento por el monto total y dividiéndolo por 100. Luego, se calcula el monto con el descuento aplicado restando el descuento al monto total.

# Luego, se utiliza la función calcular_monto_con_descuento para calcular y mostrar el monto que la persona gastó al comprar 4 kilogramos de vacío con un descuento del 5% sobre el precio total.