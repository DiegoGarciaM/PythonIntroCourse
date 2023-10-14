# Ademas, en python y en otros lenguajes de programacion podemos crear listas dinamicas
# Las listas dinamicas, o solo listas, son arreglos de datos que podemos modificar
# Podemos agregar o quitar valores, hacerlas mas grandes o chicas, modificarlas en general

list_var = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Luego podemos agregar elementos a la lista o retirarlos:
list_var.append(11)  # agregamos al final de la lista
list_var.pop(0)  # Quitamos el elemento en el indice 0
list_var.remove(2)  # quitamos el elemento con valor 2
list_var.insert(0, 2)  # insertamos un dos en el indice 0

# Existen muchas otras funciones que tenemos disponibles cuando trabajamos con listas
# Ademas las podemos usar de la misma manera que las tuplas en ciclos

for num in list_var:
    print(num)
