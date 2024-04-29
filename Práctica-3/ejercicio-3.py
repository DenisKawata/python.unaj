# Definir una función denominada RETORNO_MENSAJE que retorn siguiente mensaje: "Estudiando Fundamentos de Informatica en la UNAJ".
# A. ¿Cómo hago para mostrar ese mensaje en la pantalla? 

def retorno_mensaje():
    return "Estudiando Fundamentos de Informatica en la UNAJ"

mensaje = retorno_mensaje()

print(mensaje)

# En este código, la función RETORNO_MENSAJE retorna el mensaje "Estudiando Fundamentos de Informatica en la UNAJ". Luego, se asigna el valor retorno por la función a la variale MENSAJE. Fnalmente, se utiliza la función PRINT() para mostrar el  valor de la variable MENSAJE en pantalla.

# B. ¿Qué diferencia encuentra con el ejercicio anterior?

# La función IMRIMIR_MENSAJE imprime directamente el mensaje en pantalla utilizando la función PRINT(). En cambio, la función RETORNO_MENSAJE retorna el mensaje y lo asigna a la variable MENSAJE.

# C. Si tuviera que immprimir mensajes como "Estudiando Matematica 1 en la UNAJ" y "Estudiando Python en la UNAJ" utilizando lamisma función ¿Cóm la modificarias?

def retorno_mensaje(curso):
    return "Estudiando" + curso + "en la UNAJ"

mensaje1 = retorno_mensaje("Matematica 1")
mensaje2 = retorno_mensaje("Python")
print(mensaje1)
print(mensaje2)

# En este código, la función RETORNO_MENSAJE ahora tiene un parámetro llamado CURSO. Dentro de la función, se utiliza el operador + para concatenar el mensaje "Estudiando" con el valor de la variable CURSO y el mensaje "en la UNAJ". Luego, se retorna el mensaje concatenado. Luego de eso, se asigna el valor retorno por la función a la variable MENSAJE. Fnalmente, se utiliza la función PRINT() para mostrar el  valor de la variable MENSAJE en pantalla.