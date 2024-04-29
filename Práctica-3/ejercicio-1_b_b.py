# B) Mencione los errores en los siguientes códigos. Justifique:
    # b)
def suma(par1, par2):
    print(par1+par2)
        print(suma(12, 10))

# La función suma(par1, par2) imprime la suma de los parámetros par1 y par2 utilizando la función print(). Sin embargo, la función no devuelve ningún valor explicitamente con la palabra clave return. Por lo tanto, cuando se intenta imprimir el resultado de la función suma(12, 10) directamente en la función print(), no se obtendrá ningún resultado y generará un error.

# Para corregir el error, se puede modificar la función suma(par1, par2) para que devuelva el resultado en el lugar de imprimirlo directamente. Luego,puedes imprimir el resultado utilizando la función print() en la linea separada. Por ejemplo:

# def suma(par1, par2):
#     return par1+par2

# print(suma(12, 10))

# Con la correción, la función suma(par1, par2) devolverá el resultado de la suma de par1 y par2, y luego se imprimirá ese resultado la función print().