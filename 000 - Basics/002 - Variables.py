## Variables ##

variable_tipo_cadena = "Mi variable tipo cadena"
print(variable_tipo_cadena)

variable_tipo_int = 13
print(variable_tipo_int)

cambio_de_int_a_cadena = str(variable_tipo_int)
print(cambio_de_int_a_cadena)
print(type(cambio_de_int_a_cadena))

variable_tipo_bool = False
print(variable_tipo_bool)

# Concatenación de variables en un print
print(variable_tipo_cadena, variable_tipo_int, variable_tipo_bool)
print("Este es el valor de:", variable_tipo_bool, variable_tipo_int, variable_tipo_cadena)

# Longitud de una variable
print(len(variable_tipo_cadena))

# Inputs
nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
print(nombre)
print(edad)
print("Te llamas ", nombre, " y tienes ", edad, " años")

# Forzar el tipo de variable?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))