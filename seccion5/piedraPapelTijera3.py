# Podemos usar nuestro conocimiento de colecciones para mejorar nuestro juego
import random

player_score = 0
pc_score = 0


# Podemos usar un diccionario para asignar un valor a cada opcion
# Ahora no necesitariamos ese bloque de if que es complicado de leer
def get_input():
    # Usamos un diccionario en el que las llaves son las palabras, y el valor es un numero
    options = {'rock': 1, 'paper': 2, 'scissors': 3}
    player_string = input('Write "rock", "paper" or "scissors", or "exit" to quit: ').lower()
    # La funcion get me permite tomar el valor del diccionario, o un default si la llave no esta
    return options.get(player_string, -1)


def get_winner(pc, player):
    if pc == player:
        return 0
    elif pc == player + 1 or pc == player - 2:
        return 1
    else:
        return 2


# Podemos usar una logica similar para evitarnos tantos if en esta funcion
def get_pc_play():
    play = random.randint(1, 4)
    options = {1: 'rock', 2: 'paper', 3: 'scissors'}
    print(f'I choose {options.get(play)}!')
    return play


print("Let's play rock, paper or scissors, you will play against me!")
player = get_input()
while player != 4:
    if player == -1:
        print("You didn't type a valid input, let's try again")
    else:
        pc = get_pc_play()
        winner = get_winner(pc, player)
        if winner == 0:
            print("It's a tie!")
        elif winner == 1:
            print("I win!")
            pc_score += 1
        else:
            print("You win!")
            player_score += 1
    player = get_input()


print("Final score:")
print(f"Player score: {player_score}")
print(f"PC score: {pc_score}")
