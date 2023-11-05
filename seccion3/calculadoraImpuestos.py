# Aplicacion simple para hacer calculos matematicos
# Necesitamos preguntar al usuario por el monto por el cual quiere calcular
# Luego vamos a preguntar al usuario cual es el porcentaje de impuestos

amount = input("Give me the base amount of money: ")
tax = input("Give me the tax percentage to be added to that amount: ")

# Ahora el problema, cuando usamos "input" el dato que se guarda es un string
# Para poder hacer calculos matematicos tenemos que convertir a numeros
# Como el usuario puede usar punto decimal, vamos a usar el tipo "float"

amount = float(amount)
tax = float(amount)


# Ahora podemos calcular la cantidad sumando el porcentaje de impuestos
total = amount + (amount * tax / 100)

# Luego de esto se muestra el resultado en pantalla con un mensaje
print("The total amount plus tax is: " + total)
