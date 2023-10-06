# Cuando hacemos un ciclo con while, normalmente debemos tener una variable o condicion de salida
# Esos ciclos son utiles cuando no sabemos cuantas veces vamos a repetir
# Cuando si sabemos cuantos ciclos necesitamos podemos usar un ciclo for
# En el ciclo for la variable de control ya esta incluida, por ejemplo:

for num in range(0, 10):
    print(num)


# En este caso por cada numero en el rango de 0 a 10 (sin incluir 10) se asigna a la variable num
# Usamos la funcion range, que nos hace iterar entre dos numeros, puede funcionar con una lista

for num in [1, 2, 3, 4, 5]:
    print(num)

# El codigo que este dentro del for se repite por cada elemento de la lista, y se asigna a num.
# Incluso puede funcionar con listas con otro tipo de datos:

for word in ['Hello', 'From', 'Python']:
    print(word)

# Y como en python las string son arreglos de caracteres, incluso se puede usar un string:
for letter in "This is a string":
    print(letter)
