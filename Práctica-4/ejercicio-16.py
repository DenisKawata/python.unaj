# La aplicación de la tarjeta SUBE permite revisar los saldos día a día y Marcos decidió ver sus saldos de la semana y anotó lo siguiente:

# Lunes: $ 15 | Martes: $ -21 | Miércoles: $ -41 | Jueves: $ 109 | Viernes: $ 109

# Teniendo en cuenta el registro, definir 3 funconees que permitan mostrar lo siguiente.

# a) ¿Cuánto gastó de lunes a martes?¿de martes a miércoles?
# b) ¿Cuánto dinero cargó el miércoles para tener el saldo del jueves?
# c) Cálcule el promedio gastado en los 5 días

# a) Calcular el gasto de lunes a martes y de martes a miércoles
def calcular_gasto(saldo_inicial, saldo_final):
    gasto = saldo_inicial - saldo_final
    return gasto

saldo_lunes = 15
saldo_martes = -21
saldo_miercoles = -41

gasto_lunes_martes = calcular_gasto(saldo_lunes, saldo_martes)
gasto_martes_miercoles = calcular_gasto(saldo_martes, saldo_miercoles)

print("El gasto de lunes a martes es: " + str(gasto_lunes_martes))
print("El gasto de martes a miércoles es:" + str(gasto_martes_miercoles))

# b) Calcular el dinero cargado el miércoles para tener el saldo del jueves
def calcular_carga(saldo_inicial, saldo_final):
    carga = saldo_final - saldo_inicial
    return carga

saldo_jueves = 109

carga_miercoles = calcular_carga(saldo_miercoles, saldo_jueves)

print("El dinero cargado el miércoles para tener el saldo del jueves es: " + str(carga_miercoles))

# c) Calcular el promedio gastado en los 5 días
def calcular_promedio_gasto(gastos):
    promedio = sum(gastos) / len(gastos)
    return promedio

gasto_viernes = 109

gastos = [gasto_lunes_martes, gasto_martes_miercoles, 0, 0, gasto_viernes]  # Agregar 0 para los días sin gasto registrado

promedio_gasto = calcular_promedio_gasto(gastos)

print("El promedio gastado en los 5 días es: " + str(promedio_gasto))

# En este código, se definen tres funciones para calcular diferentes aspectos relacionados con los saldos de la tarjeta SUBE:


# - La función calcular_gasto recibe un saldo inicial y un saldo final, y calcula el gasto restando el saldo final al saldo inicial.
# - La función calcular_carga recibe un saldo inicial y un saldo final, y calcula la cantidad de dinero cargada restando el saldo inicial al saldo final.
# - La función calcular_promedio_gasto recibe una lista de gastos y calcula el promedio dividiendo la suma de los gastos entre la cantidad de días.

# Luego, se utilizan estas funciones para calcular y mostrar los resultados solicitados:


# - Se calcula el gasto de lunes a martes y de martes a miércoles utilizando la función calcular_gasto.
# - Se calcula la carga del miércoles utilizando la función calcular_carga.
# - Se calcula el promedio de gastos en los 5 días utilizando la función calcular_promedio_gasto.
