import random

'''
function LOAD WORD opens the document of words.txt and reads every line.
next, it splits each word at the comma and creates a list of items
finally, it selects a random word, assigns it as the secret word, and returns that word.
'''
def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') 
    secret_word = random.choice(words_list)
    #print (secret_word)
    return secret_word


'''
function GET GUESS prompts the user to guess a letter
returns the guessed letter
'''
def get_guess():
    guess = input("Guess a letter! --> ")
    return guess



'''
function CHECK GAME STATE 
'''
def check_game_state(game_active):
    if game_active == False:
        print("Would you like to play again?")
        play_again = input("yes/no --> ")
        if (play_again == "yes"):
            already_guessed = []
            game_win = False
            game_lose = False
            secret_word = load_word()
            secret_word_length = len(secret_word)
            blank_spaces = []
            friendly_doodle(secret_word)
        
        #complete the function



'''
function CHECK WIN
'''

def check_win():
    if "_ " not in blank_spaces:
        print("You win!")
        game_active = False

    else:
        game_active = True
    
    return game_active


'''
function CHECK LOSE
'''

def check_lose():
    num_guesses = 10
    if num_guesses < 0:
        print("You lose.")
        game_active = False
    
    else:
        game_active = True
    
    return game_active




'''
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
'''



'''
function CHECK GUESS takes in the guess and number of guesses
1. first, it checks to ensure that the guess is a letter
2. next, it checks to see if the user has already guessed that letter
3. after that, it checks to see if the letter is in the secret word &
displays the letter in the blank space
4. finally, if the letter is not in the word, it subtracts a guess 
'''

def check_guess(guess):

    #first check to see if the guess is a letter
    #if not, print an error message
    if guess.isalpha() == False: 
        print("Invalid input. Enter a letter and guess again!")

    #check the guess against the list of already guessed letters
    elif guess in already_guessed:
        print("You already guesssed that letter. Guess again!")

    #if it passes above, checks to see if the guess is in the secret word
    elif guess.lower() in secret_word:
        already_guessed.append(guess)  #append to the already guessed list
        i=0
        while i < secret_word_length: #compare the guess to every letter
            if guess == secret_word[i]:
                print("You got it!")
                blank_spaces[i] = guess #wherever it matches, replace the blank space with the letter
            i += 1

    #if the guess is valid but not in the secret word
    #append the guess to the already guessed list
    #print that it is not in the word & number of guesses remaining
    else:
        already_guessed.append(guess)
        print("Nope, not that one.")
        print(f"You have __ guesses remaining. Guess again.")
    
    




'''
function DISPLAY SPACES shows a space for each letter of the secret word
'''    
def display_spaces():
    i = 0
    while i < secret_word_length:
        blank_spaces.append("_ ")
        i += 1
    display = ''.join(blank_spaces)
    print (display)
    return(blank_spaces)


'''
function DISPLAY WORD used to show the blank spaces & letters after game is started
'''    
def display_word():
    display = ''.join(blank_spaces)
    print (display)


'''
function FRIENDLY DOODLE runs the game
'''
def friendly_doodle(secret_word):

    while (game_win == False or game_lose == False): 

        #Ask the player to guess a letter
        guess = get_guess()

        #Check to see if the input is in the word, is valid, etc.
        check_guess(guess)

        #Show the guessed word
        print("")
        display_word()

        #Check if the game has been won or lost
        game_active = check_win()
        check_game_state(game_active)
        game_active = check_lose()
        check_game_state()

        #check_game_state(game_win, score, secret_word_length)

    




'''
------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------
                                 Begin playing the game!
------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------
'''

#initialize variables to start the game
score = 0
already_guessed = []
game_win = False
game_lose = False
secret_word = load_word()
secret_word_length = len(secret_word)
blank_spaces = []


#Welcome to the game
print ("")
print("Welcome to friendly doodle!") 
print("This is a game where you compete to guess a mystery word before the friendly doodle finishes drawing itself.")
print("Each space represents a letter in the word.")
print("Ready? Let's play!")
print("")

print("Here's your first word:")
display_spaces()

#Run the game
friendly_doodle(secret_word)

















