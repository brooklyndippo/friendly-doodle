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
    guess = input("Guess a letter!")
    return guess

def game_state(bad_guess):
    if bad_guess > 7:
        game_lose = True

def check_game_state(game_win, score, secret_word_length):
    if game_win == True:
        score += (secret_word_length * 100)
        print (f"Your score is {score}")
        game_win = False
        return score
    else:
        pass


def check_guess(guess):
    if guess in already_guessed:
        print("You already guesssed that letter. Guess again!")
    elif guess in secret_word:
        already_guessed.append(guess)
        i=0
        while i < secret_word_length:
            if guess == secret_word[i]:
                print("You got it!")
                blank_spaces[i] = guess
        pass #replace corresponding underscore with guess
    else:
        already_guessed.append(guess)
        bad_guess += 1
        print("Nope, not that one. Guess again.")
    display_word()
    get_guess()


def display_spaces(secret_word_length):
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
    print("Welcome to friendly doodle! This is a game where you compete to guess a mystery word before the friendly doodle finishes drawing itself. Ready? Let's play!")

    while (game_win == False or game_lose == False): 

        #Ask the player to guess a letter
        guess = get_guess()

        #Check to see if the input is in the word, is valid, etc.
        check_guess(guess)

        #Show the guessed word
        display_word()

        #Check the game status
        check_game_state()


#initialize variables to start the game
score = 0
bad_guess = 0
already_guessed = []
game_win = False
game_lose = False
secret_word = load_word()
secret_word_length = len(secret_word)
blank_spaces = []
display_spaces(secret_word_length)
friendly_doodle(secret_word)





















def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''


    #TODO: show the player information about the game according to the project spec
    print("Welcome to Friendly Doodle, a game in which you try to guess a mystery word BEFORE the doodle is complete!")

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost




def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in letters_guessed:
        if letter not in secret_word:
            pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word

    pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''


    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
#secret_word = load_word()
spaceman(secret_word)