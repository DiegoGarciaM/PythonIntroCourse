# Ademas de las listas y las tuplas, existen mas colecciones que podemos usar en ciertas ocasiones
# Un ejemplo son los sets, que son similares a las listas, pero no permiten que se repitan valores
# Por la manera en que se guardan los sets en la memoria, el orden de los valores puede cambiar
# Por eso el principal uso de los sets es para saber si hemos visto un valor o no
# Es decir, solo para saber si un valor ya esta en el set o no, y son muy eficientes

set_var = {1, 2, 3, 4, 5, 6}

# Por ejemplo, digamos que queremos saber si hay un 5 en el set:
if 5 in set_var:
    print("there is a 5 in the set")

# Tecnicamente se puede hacer lo mismo, pero en realidad un set es mas rapido y usa menos memoria
# Ademas podemos agregar elementos al set:
set_var.add(7)

# Si el set ya contiene el elemento, el elemento simplemente no se agrega, ahorrando memoria

# Un truco interesante es que podemos usar un set para eliminar elementos repetidos en una lista
# Simplemente convertimos la lista a un set, luego de regreso a la lista
has_repeated = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
converted_to_set = set(has_repeated)
no_repeated = list(converted_to_set)

print(no_repeated)


# En python tambien podemos usar algo llamado diccionarios
# En los diccionarios los valores se asocias con una llave
# La existencia de las llaves hace que podamos buscar los datos facilmente
dict_var = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5}

# Podemos acceder a las llaves de manera individual como una lista, o a los valores
# Y para acceder a algun dato podemos hacerlo con la llave en lugar de un indice
print(f"the first value in the dictionary is: {dict_var['first']}")
