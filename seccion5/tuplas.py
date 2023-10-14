# En python, como en otros lenguajes de programacion, es muy util guardar varios elementos.
# La idea es simple, una variable es ponerle nombre a un lugar en la memoria que podemos modificar
# De la misma manera, podemos poner un nombre a la memoria donde guardamos varios elementos
# Es decir, podemos guardar mas de un dato en una variable

# La manera mas sencilla de hacer esto es con las tuplas (tuples)
# Es un arreglo de datos estatico, es decir que no se puede cambiar despues de que lo creamos

tuple_var = ("data1", "data2", "data3")

# Luego podemos pasar esa variable y usarla en el codigo de manera mas sencilla, solo es una
# Si queremos acceder a alguno de los datos, lo hacemos por el indice que tiene en la tupla
# Los indices en Python, como en casi todos los lenguajes de programacion, comienzan en 0

print(f"The first data point in the tuple is {tuple_var[0]}")

print(f"The second data point in the tuple is {tuple_var[1]}")


# Ademas podemos usar las tuplas de manera muy sencilla en un ciclo for, por ejemplo:
days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday" "sunday")

for day in days:
    print(day)

# Ademas hay funciones que funcionan con las tuplas y otras colecciones
# Por ejemplo, podemos tomar un elemento al azar de manera muy sencilla


def get_random_day():
    from random import choice
    days_local = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday" "sunday")
    return choice(days_local)


print(f"A random day is: {get_random_day()}")
