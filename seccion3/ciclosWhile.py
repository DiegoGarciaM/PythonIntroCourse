# Otra manera que tenemos de controlar nuestro codigo son los ciclos
# Con ciclos podemos repetir instruccione cierto numero de veces
# Lo importante a considerar es el numero de ciclos que queremos
# Es decir, cuales son las condiciones para romper un ciclo

# Podemos usar el comando "while" para repetir instrucciones
# Mientras que se cumpla una condicion, entraremos en el codigo del "while"
# Por ejemplo, podemos poner en consola los numeros del 1 al 10:


print("Numbers from 1 to 10 using cycles")

num = 1  # Comenzamos con una variable para poder comparar en el "while"

while num <= 10:  # Vamos a repetir mientras el numero sea menor o igual a 10
    print(num)  # ponemos el numero en la consola
    num += 1  # Asi podemos sumar 1 al numero, de otra manera nunca terminamos


# El que tengamos una condicion nos permite decidir como queremos terminar
# Podemos tambien hacer cosas como poner en consola solo los numeros pares:


print("Even numbers from 1 to 10")

num = 2  # Comenzamos con el 2 para comenzar con un numero par

while num <= 10:
    print(num)
    num += 2  # Ahora sumamos dos, para asegurar que el numero sea par
