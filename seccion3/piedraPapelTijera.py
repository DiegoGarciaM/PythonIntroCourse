# Este es un ejemplo de un juego sencillo de piedra papel o tijera
# Se juega contra la computadora, se cuenta el puntaje
# El jugador decide cuando se termina el juego

# Primero vamos a pensar en como puede la computadora escoger su jugada
# Una manera sencilla es con un numero al azar, 1, 2, o 3
# Generar un numero al azar es sencillo, usando una libreria de python
# Para usar esta herramienta de python podemos usar la libreria "random"
import random

# Despues vamos a definir variables que vamos a usar:
# Necesitamos una variable para contar los puntos del jugador
player_score = 0
# Necesitamos una variable para el puntaje de la computadora:
pc_score = 0

# Lo primero que quiero que aparezca en la pantalla es un mensaje:
print("Let's play rock, paper or scissors, you will play against me!")

# Para el juego, podemos preguntar al jugador por una opcion de jugada,
# si el jugador escribe exit, el juego termina
# Se guarda la entrada en una variable
# Algo bueno de python es que podemos usar comillas dobles o simples
# Dependiendo de la situacion, en ambos casos lo que se guarda es un string.
player = input('Write "rock", "paper" or "scissors", or "exit" to quit: ')

# Para evitar errores por el usuario, pasamos a minusculas
player = player.lower()
# Ahora podemos poner todo el juego en un ciclo, que termine con el 'quit'
while player != 'quit':
    # Si estamos aqui el jugador ya elijio algo, ahora le toca al PC
    # El PC elije 1, 2, o 3 (piedra, papel o tijera)
    pc = random.randint(1, 4)
    # Ahora toca hacer todas las comparaciones para ver quien gana
    if pc == 1:
        print("I choose rock!")
        if player == 'rock':
            print("It's a tie!")
        elif player == 'paper':
            print("You win!")
            player_score += 1
        else:
            print("I win!")
            pc_score += 1
    elif pc == 2:
        print("I choose paper!")
        if player == 'rock':
            print("I win!")
            pc_score += 1
        elif player == 'paper':
            print("It's a tie!")
        else:
            print("You win!")
            player_score += 1
    else:
        print("I choose scissors!")
        if player == 'rock':
            print("You win!")
            player_score += 1
        elif player == 'paper':
            print("I win!")
            pc_score += 1
        else:
            print("It's a tie!")

# Ahora podemos pedir la siguiente jugada al jugador
    player = input('Write "rock", "paper" or "scissors", or "exit" to quit: ')
    player = player.lower()


# Si estamos fuera del while, el juego termino, podemos poner el marcador
print("Final score:")
print(f"Player score: {player_score}")
print(f"PC score: {pc_score}")
