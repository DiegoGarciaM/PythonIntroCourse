# Vamos a rehacer el juego de piedra papel y tijera con funciones, vara ver si puede mejorar
import random

# Vamos a mantener las variables para el puntaje como globales, ya que se usan en muchos sitios
player_score = 0
pc_score = 0


# Ahora hay que pensar en que operaciones podemos encapsular en funciones
# Las mejores operaciones para guardar en funciones son las que repetimos varias veces
# Por ejemplo, cuando pedimos al jugador que nos de su jugada
# Ademas podemos convertir la entrada del jugador a un numero, para poder compararlos mas facil:
def get_input():
    player_string = input('Write "rock", "paper" or "scissors", or "exit" to quit: ').lower()
    if player_string == 'rock':
        return 1
    elif player_string == 'paper':
        return 2
    elif player_string == 'scissors':
        return 3
    elif player_string == 'exit':
        return 4
    else:
        return -1  # podemos usar esto por si la persona escribe algo mal o que no es una opcion


# Tambien podemos hacer una funcion que nos ayude a comparar las jugadas
# Aunque solo hagamos algo una vez, es bueno separar acciones, nos ayuda a que el codigo mejore
# Esta funcion toma el dato del pc, y el del jugador
# Y para evitar que la funcion altere valores globales, solo retorna un valor, 1 para pc, 2 jugador
def get_winner(pc, player):
    # Como los valores son 1, 2, o 3, el ganador es mayor por uno o mejor por dos
    # Podemos revisar primero el caso en el que es un empate:
    if pc == player:
        return 0
    elif pc == player + 1 or pc == player - 2:
        return 1
    else:
        return 2


# Tambien seria bueno que cuando el PC haga su jugada, le diga al jugador que elijio
def get_pc_play():
    play = random.randint(1, 4)
    if play == 1:
        print('I choose rock!')
    elif play == 2:
        print('I choose paper!')
    else:
        print('I choose scissors!')
    return play


# Ahora que tenemos nuestras funciones definidas podemos escribir el programa principal
print("Let's play rock, paper or scissors, you will play against me!")

# La logica es casi igual, comenzamos con un saludo y luego pedimos el primer valor al jugador
player = get_input()

# Ahora podemos poner todo el juego en un ciclo, que termine con el 'quit' que ahora es 4
while player != 4:
    # Si el jugador escribe algo incorrecto, podemos decirle y saltar al siguiente ciclo
    if player == -1:
        print("You didn't type a valid input, let's try again")
    else:

        # Si estamos aqui el jugador ya elijio algo, ahora le toca al PC
        # El PC elije 1, 2, o 3 (piedra, papel o tijera)
        pc = get_pc_play()
        # Ahora toca hacer todas las comparaciones para ver quien gana
        winner = get_winner(pc, player)
        if winner == 0:
            print("It's a tie!")
        elif winner == 1:
            print("I win!")
            pc_score += 1
        else:
            print("You win!")
            player_score += 1

# Ahora podemos pedir la siguiente jugada al jugador
    player = get_input()


# Si estamos fuera del while, el juego termino, podemos poner el marcador
print("Final score:")
print(f"Player score: {player_score}")
print(f"PC score: {pc_score}")
