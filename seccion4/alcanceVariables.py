# En programacion, un problema comun es el del alcance de las variables
# No todas las variables deben ser accesibles desde cualquier parte de un programa
# Cuando declaramos una variable fuera de cualquier funcion, esa variable es global
# Es decir, la podemos usar desde cualquier parte del codigo, funciones incluidas


global_variable = "This is a global variable"

# En cambio las variables declaradas dentro de las funciones, y sus parametros solo existen ahi


def myFunc(parameter):
    local_variable = "This is a local variable, only for the function"
    print("I can access the local variable here: ", local_variable)
    print("I can access the parameter here: ", parameter)


print("I cannot access the parameter here")
print("I cannot access the local variable here")
print("I can access the global variable here")

# Hay muchas razones para esto:
# Una de las buenas practicas en programacion es la division de responsabilidades
# Cuando un programa es grande, no quieres que partes que no tienen relacion compartan datos
# Esto puede llevar a muchos errores y dificultad para modificar el codigo
# Lo mejor es dividir el codigo en funciones (o clases) que se encargen de una tarea
# Entonces el programa principal solo se encarga de llamar a las funciones adecuadas
