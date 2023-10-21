# El ahorcado es un juego muy sencillo de hacer a base de listas o colecciones
# El punto es que el jugador no sepa que palabra jugara, para eso podemos usar una lista o tupla
# Para ahorrar espacio en el archivo con la logica del juego, podemos poner eso en otro archivo
# Luego importamos ese archivo como hacemos con otras librerias de python.

# El juego va a ocurrir dentro de un ciclo, y va a haber 5 intentos antes de que el jugador pierda
attempts = 5
# Ahora podemos pensar en las otras variables que va a necesitar el juego
# Por ejemplo una lista de letras que vayan siendo usadas
# Y como solo me interesa saber si ya fueron usadas, puede ser un set
used_letters = set()  # Asi podemos crear un set vacio

# Tambien podemos crear un set con las palabras que ya pasaron, para no repetir y mostrar al final
used_words = set()


# Vamos a crear una funcion para escoger una palabra, la vamos a necesitar despues
def choose_word():
    from palabrasAhorcado import words  # Podemos importar solo la variable que queremos
    from random import choice
    if len(used_words) == len(words):
        return 'USED_ALL_WORDS'
    random_word = choice(words)
    while random_word in used_words:
        random_word = choice(words)
    return random_word


# EL juego debe tomar la palabra, y ponerla como guiones, para eso podeos hacer otra funcion
def get_hidden_word(word):
    hidden = []  # podemos hacerlo con una lista, agregamos un guion por cada letra de la palabra
    for leter in word:
        hidden.append('_')
    return hidden


# Tambien podemos definir una funcion para pedir letras al usuario, para ahorrar trabajo despues
# Podemos aprovechar para validar, por ejemplo, que solo haya una letra y hacerla minuscula
def get_letter():
    # Le avisamos a la funcion que vamos a usar una variable global
    global used_letters
    ltr = ""
    is_valid = False
    while not is_valid:
        ltr = input("Enter your next letter: ").lower()
        if len(ltr) != 1:
            print("Just enter one letter...")
        elif ltr in used_letters:
            print("That letter has already been used")
        else:
            used_letters.add(ltr)
            is_valid = True
            break
    return ltr


# Podemos crear una funcion para poner las letras en el lugar adecuado de la lista de guiones
def fill_letters(letter_list, original_word, letter):
    for index in range(len(letter_list)):
        if letter == original_word[index]:
            letter_list[index] = letter

    return letter_list


# Ahora podemos comenzar el ciclo principal del juego
# El juego va a mostrar un mensaje de bienvenida, luego comenzara
print("Welcome to the hangman game!\n******************\nLet's begin!")
word = choose_word()  # seleccionamos la palabra
hidden_word = get_hidden_word(word)  # conseguimos la palabra como guiones

while attempts > 0:
    # Vamos a comenzar la ronda poniendo el estado actual en pantalla y pidiendo una letra
    print(f"\n\nThe word is: {hidden_word}")
    letter = get_letter()
    if letter not in word:
        attempts -= 1
        print(f"Wrong!, you have {attempts} left!")
    else:
        print("Correct!!!")
        hidden_word = fill_letters(hidden_word, word, letter)
        # Tenemos que revisar si la palabra ya termino
        if '_' not in hidden_word:
            used_words.add(word)
            print(f"\n\nYou won this round! the word was: {word}")
            # Podemos checar si el jugador quiere jugar otra ronda
            another = input("Would you like to play another round? (y/n)").lower()
            if another == 'n':
                break
            # Ahora podemos comenzar otra ronda, o ver si ya no hay palabras por usar
            word = choose_word()
            hidden_word = get_hidden_word(word)
            attempts = 5
            if word == 'USED_ALL_WORDS':
                print('No more available words! You Win!!!')
                break


# Podemos poner la ultima palabra en pantalla para que se vea cuando el jugador pierda o salga
print(f"The last word was: {word}")
