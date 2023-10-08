# Las funciones son una manera de tener codigo que podemos reusar en cualquier momento.
# A diferencia de los ciclos, el codigo no se ejecuta de manera automatica.
# En python, las funciones se definen con "def", y se usa un parentesis, por si necesita datos.

def myFunc():
    print("This is the code inside the function")


# Si solo la definimos, la funcion no se ejecuta, para que suceda hay que llamarla:
myFunc()


# Las funciones pueden contener una gran cantidad de codigo que luego no hay que repetir
# Ademas, podemos dar datos de entrada para las funciones, llamados parametros
# Estos actuan como variables que solo existen dentro de la funcion, no les importa el exterior


def calculateTax(amount, tax):
    total = amount + (amount * tax / 100)
    print(f"Total amount plus tax: {total}")


# Ahor apodemos llamar la funcion y hacer el calculo con diferentes valores cada vez:
# Comenzamos a ver el poder de las funciones, que nos ayudan a organizar nuestro codigo
calculateTax(1000, 15)
calculateTax(2000, 10)


# Por ultimo, las funciones pueden tener un valor de salida
def getTotalAmount(amount, tax):
    return (amount + (amount * tax / 100))


# De esta manera podemos realizar operacinoes que retornen algun valor para usarlo despues
total = getTotalAmount(1000, 15)
print(getTotalAmount(2000, 10))
