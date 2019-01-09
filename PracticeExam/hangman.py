""" 
Write a Python program that allows a user to play the game Hangman. 
In the game, the computer selects a word from a collection of words and the user tries 
to guess the word by iteratively suggesting its individual letters.  
In this implementation of the game the following holds: 
    - The user has at most 12 tries when guessing individual letters of a word.
    - The collection of words from which the computer selects is always the same each time the game is played.
      The word should be selected from the collection by using the function random.choice().

Info on randomchoice():

random.choice(seq)
Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.

The start of the main program is given as well as some constants.  You should use both and you are 
not allowed to change it.  At the start, the program asks for a seed for the random generator, 
chooses a word which the user needs to guess, and prints out some instructions.  Example:
Random seed: 10
The word you need to guess has 3 characters
Word to guess: - - -

Thereafter, the user can input suggestions for individual letters until the correct word 
has been guessed or the number of tries has been reached.  In each iteration, a message is
printed if the input letter has been suggested before (this error does not affect the number of tries):

You have already guessed that letter!

If no error is found, then the program prints: 
You guessed correctly! or The letter is not in the word!

Moreover, in each iteration a message is printed showing how often the user has 
suggested a letter, in the following manner:
You are on guess 1/12

In the end, the program prints:
You won! or You lost! The secret word was xxx
"""

import random

# Constants to be used in the implementation
WORD_LIST = [
"lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
           ]
MAX_GUESS = 12
CHAR_PLACEHOLDER = '-'

def random_seed():
    """
    Creates pseudorandom int
    based on user input
    """
    seed = int(input("Random seed: "))
    random.seed(seed)

def print_hide_word(correct_word,guesses_set):
    """
    Prints out character placeholder
    for every non-guessed letter,
    and any correctly guessed letters
    """
    revealed_word = []
    correct_word = list(correct_word)

    for letter in correct_word:
        if letter in guesses_set:
            revealed_word.append(letter)
        else:
            revealed_word.append(CHAR_PLACEHOLDER)
    revealed_word = " ".join(revealed_word)
    print("Word to guess: {}".format(revealed_word))

def check_win(correct_word,guesses_set):
    """
    If all letters in the correct word
    are found in the set of guessed letters,
    then the player has obviously won
    """
    correct_word_set = set(correct_word)
    if correct_word_set.issubset(guesses_set):
        print("You won!")
        print_hide_word(correct_word,guess_set)
        quit()
    

def make_guess_set(guess_set):
    """ 
    Prompts user for new guess
    and adds it to set of
    guessed letters
    """    
    current_guess = input("Choose a letter: ")
    if len(current_guess) == 1:
        guess_set.add(current_guess)
        return guess_set
    else:
        print("Invalid entry")
        return make_guess_set(guess_set)

def print_is_letter_in_word(guess_set,guess_set_copy,correct_word):
    """
    Compares set of current guesses with set of previous guesses.
    Then compares differences between those with the set
    of the letters in the correct word.
    """
    difference = guess_set.difference(guess_set_copy)
    intersection = guess_set.intersection(guess_set_copy)
    correct_word_set = set(correct_word)

    if len(guess_set) == len(guess_set_copy):  # Check if the current and previous guess sets the same
        print("You have already guessed that letter!")
    elif difference.issubset(correct_word_set):  # Check if the new addition is in the correct word
        print("You guessed correctly!")
    elif not difference.issubset(correct_word_set):  # Check if the new addition is not in the correct word
        print("The letter is not in the word!") 
        
        
# Main program starts here

# Choose a random word from the word list, based on the
# generated random seed.
random_seed()
correct_word = random.choice(WORD_LIST)

# Save guessed letters in set
guess_set = set()
tries = 0
print("The word you need to guess has {} characters".format(len(correct_word)))
while tries != MAX_GUESS:
    guess_set_copy = guess_set.copy()  # Save previous iteration of guesses
    print_hide_word(correct_word,guess_set)  # Formats how hidden/revealed letters are printed
    guess_set = make_guess_set(guess_set)  # User makes a guess
    print_is_letter_in_word(guess_set,guess_set_copy,correct_word)  # Msg if letter was right or not
    check_win(correct_word,guess_set)  # Check if user has guessed all correct letters
    tries += 1
    if guess_set == guess_set_copy:  # User not penalized for guessing same letter
        tries -= 1
    print("You are on guess {}/{}".format(tries,MAX_GUESS))

# After tries == MAX_GUESS, player has lost
print_hide_word(correct_word,guess_set)
print("You lost! The secret word was {}".format(correct_word))
