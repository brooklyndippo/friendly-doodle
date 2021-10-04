import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    print (secret_word)
    return secret_word


def get_guess():
    guess = input("Guess a letter! --> ")
    return guess

def game_state(num_guesses):
    if num_guesses < 1:
        game_lose = True

def check_game_state(game_win, score, secret_word_length):
    if game_win == True:
        score += (secret_word_length * 100)
        print (f"Your score is {score}")
        game_win = False
        return score
    else:
        pass


def check_guess(guess, num_guesses):

    #first check to see if the guess is valid
    if guess.isalpha() == False: 
        print("Invalid input. Enter a letter and guess again!")

    
    elif guess in already_guessed:
        print("You already guesssed that letter. Guess again!")

    elif guess.lower() in secret_word:
        already_guessed.append(guess)
        i=0
        while i < secret_word_length:
            if guess == secret_word[i]:
                print("You got it!")
                blank_spaces[i] = guess
            i += 1
    else:
        already_guessed.append(guess)
        num_guesses -= 1
        print("Nope, not that one.")
        print(f"You have {num_guesses} guesses remaining. Guess again.")
    

def display_spaces():
    i = 0
    while i < secret_word_length:
        blank_spaces.append("_ ")
        i += 1
    display = ''.join(blank_spaces)
    print (display)
    return(blank_spaces)

def display_word():
    display = ''.join(blank_spaces)
    print (display)


def friendly_doodle(secret_word):
    
    #Welcome to the game
    print("Welcome to friendly doodle!") 
    print("This is a game where you compete to guess a mystery word before the friendly doodle finishes drawing itself.")
    print("Each space represents a letter in the word.")
    print("Ready? Let's play!")
    print("Here's your first word:")
    display_spaces()

    while (game_win == False or game_lose == False): 

        #Ask the player to guess a letter
        guess = get_guess()

        #Check to see if the input is in the word, is valid, etc.
        check_guess(guess, num_guesses)

        #Show the guessed word
        print("")
        display_word()

        #Check if the game has been won or lost
        check_game_state(game_win, score, secret_word_length)


#initialize variables to start the game
score = 0
num_guesses = 7
already_guessed = []
game_win = False
game_lose = False
secret_word = load_word()
secret_word_length = len(secret_word)
blank_spaces = []
friendly_doodle(secret_word)






















