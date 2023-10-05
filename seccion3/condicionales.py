# Ademas de operaciones matematicas, podemos realizar operaciones logicas
# Es decir, operaciones que tienen como resultado un booleano (True o False)
# Podemos comparar igualdad (==) diferencia (!=) mayor o menor que (>, <)
# Podemos comparar mayor o igual, menor o igual (>=, <=)
# Podemos combinar comparaciones usando "and" o "or"


result = 5 == 5  # 5 es igual a 5, por lo tanto se guarda True en la variable
result = 5 != 5  # 5 es igual a 5, por lo tanto se guarda False en la variable

result = 3 < 5  # 3 es menor a 5, por lo tanto se guarda True en la variable

result = 5 == 5 and 3 < 5  # El resultado de la expresion es True
result = 5 == 5 and 3 > 5  # El resultado de la expresion es False
result = 5 == 5 or 3 > 5  # El resultado de la expresion es True

# Ahora podemos poner condiciones en el codigo que queremos ejecutar usando if
# Por ejemplo, vamos a imprimir a la consola si un numero es par o impar
# Podemos usar la operacion "modulo", que nos da el sobrante de la division

# Vamos a pedir un numero en consola, podemos convertir a int directamente
num = int(input("Give me an integer number: "))
# Calculamos el sobrante de dividir entre 2, lo guardamos en una variable
left_over = num % 2

# Ahora ponemos algo en consola dependiendo si es par o no
# Es decir, si el sobrante es 0, entonces es par
# Podemos hacer algo en caso de que la comparacion de False usando un "else"
if left_over == 0:
    print("the number is even")
else:
    print("the number is odd")
