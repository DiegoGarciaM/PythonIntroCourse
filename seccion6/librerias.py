# Ya hemos visto como podemos importar librerias a python, tanto del lenguaje como ramdon
# Como propias, como la lista de palabras que usamos en el ahorcado
# De esta manera podemos organizar nuestro codigo en modulos, con una sola responsabilidad
# Asi no tenemos el codigo en un solo lugar, y es mas facil trabajar (como con las funciones)

# Ademas, existe una gran cantidad de librerias disponibles para python que podemos instalar
# Para instalar librerias que no vienen con python podemos usar el comando pip

# Por eso siempre es buena idea investigar un poco, para saber que herramientas estan disponibles
# Vamos a poner un ejemplo de una aplicacion con una interfaz grafica
# Para eso vamos a usar una de las librerias de python llamada Tkinter
import tkinter as tk

# Todo esto lo podemos ver en la documentacion que tkinter tiene en internet
# Esa es una de las ventajas de usar librerias que ya existen para python
# No es necesario crear todo desde cero

window = tk.Tk()
window.title("My window")


window.mainloop()
