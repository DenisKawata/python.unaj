# Definir tres funciones llamadas CONVERTIR_A_DOLAR, CONVERTIR_A_EURO y CONVERTIR_A_REAL. Cada funcón recibe un parámetro que representa un monto en pesos y devuelve su conversión respectiva.

def convertir_a_dolar(monto_pesos):
    tipo_cambio_dolar = 20.0  # Supongamos un tipo de cambio fijo de 20 pesos por dólar
    monto_dolares = monto_pesos / tipo_cambio_dolar
    return monto_dolares

def convertir_a_euro(monto_pesos):
    tipo_cambio_euro = 25.0  # Supongamos un tipo de cambio fijo de 25 pesos por euro
    monto_euros = monto_pesos / tipo_cambio_euro
    return monto_euros

def convertir_a_real(monto_pesos):
    tipo_cambio_real = 4.0  # Supongamos un tipo de cambio fijo de 4 pesos por real
    monto_reales = monto_pesos / tipo_cambio_real
    return monto_reales

# Ejemplo de uso de las funciones
monto_en_pesos = 1000

monto_en_dolares = convertir_a_dolar(monto_en_pesos)
monto_en_euros = convertir_a_euro(monto_en_pesos)
monto_en_reales = convertir_a_real(monto_en_pesos)

print("El monto en dólares es: " + str(monto_en_dolares))
print("El monto en euros es: " + str(monto_en_euros))
print("El monto en reales es: " + str(monto_en_reales))

# En este código, se definen tres funciones: convertir_a_dolar, convertir_a_euro y convertir_a_real. Cada función recibe un parámetro monto_pesos, que representa un monto en pesos. Luego, se realiza la conversión dividiendo el monto en pesos por el tipo de cambio correspondiente. Finalmente, se devuelve el monto convertido.