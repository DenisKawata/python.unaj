# Reutilice la función definida anteriormente para procesar una lista de 50 personas que se ingresan desde teclado. Para cada persona, se debe informar el porcentaje de sueldo destinado a impuestos, a comida y a colegio.

def porcentaje(monto_total, monto_destinado):
    return (monto_destinado / monto_total) * 100

def porcentaje_impuestos(persona):
    return porcentaje(persona['sueldo'], persona['impuestos'])

def porcentaje_comida(persona):
    return porcentaje(persona['sueldo'], persona['comida'])

def porcentaje_colegio(persona):
    return porcentaje(persona['sueldo'], persona['colegio'])

def calcular_porcentajes(persona):
    porcentaje_imp = porcentaje_impuestos(persona)
    porcentaje_com = porcentaje_comida(persona)
    porcentaje_col = porcentaje_colegio(persona)
    return porcentaje_imp, porcentaje_com, porcentaje_col

personas = []
for i in range(50):
    sueldo = float(input(f"Ingrese el sueldo de la persona {i+1}: "))
    impuestos = float(input(f"Ingrese el monto destinado a impuestos para la persona {i+1}: "))
    comida = float(input(f"Ingrese el monto destinado a comida para la persona {i+1}: "))
    colegio = float(input(f"Ingrese el monto destinado al colegio para la persona {i+1}: "))
    persona = {
        'sueldo': sueldo,
        'impuestos': impuestos,
        'comida': comida,
        'colegio': colegio
    }
    personas.append(persona)

for i, persona in enumerate(personas):
    porcentajes = calcular_porcentajes(persona)
    print(f"Persona {i+1}:")
    print("Porcentaje de sueldo destinado a impuestos: " + str(porcentajes[0]))
    print("Porcentaje de sueldo destinado a comida: " + str(porcentajes[1]))
    print("Porcentaje de sueldo destinado al colegio: " + str(porcentajes[2]))
    print()  # Espacio en blanco para mayor claridad

# En este programa, se utiliza un bucle for para solicitar el sueldo, monto destinado a impuestos, monto destinado a comida y monto destinado al colegio para cada una de las 50 personas. Luego, se calculan y muestran los porcentajes correspondientes para cada persona.