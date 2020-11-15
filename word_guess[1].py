"""
File: word_guess.py
-------------------
Plays WordGuess!
The computer first selects a secret word at random from
a list built into the program. The program then prints out a row of dashes— one for each
letter in the secret word and asks the user to guess a letter. If the user guesses a letter that
is in the word, the word is redisplayed with all instances of that letter shown in the correct
positions, along with any letters correctly guessed on previous turns. If the letter does not
appear in the word, the user is charged with an incorrect guess. The user keeps guessing
letters until either (1) the user has correctly guessed all the letters in the word or (2) the
user has made eight incorrect guesses.
"""

import random

def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)

    
LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    string -> string
    Fn takes a word unknown to user, and allows user to play WordGuess game, and displays result of the game 
    """
    # game starts with 8 guesses
    guesses_left = INITIAL_GUESSES
    # show just dashes for letters in the word
    current_guess = "-" * len(secret_word)

    # for loop to keep track of guesses:
    while guesses_left > 0:

        # print status
        print_status(current_guess, guesses_left)

        # prompt for input
        input_letter = input("Type a single letter here, then press enter: ")

        # check if input_letter in secret_word
        if input_letter.lower() in secret_word.lower():
            # print success
            print("That guess is correct.")

            # find the index(es) where input letter can be found in the word and create a list of it
            ind_letter_in_word = list(indexes(secret_word, input_letter))

            # update current word by replacing the letters in this index(es) with input letter
            current_guess = update_word(current_guess, input_letter, ind_letter_in_word)

        else:
            print("There are no {}'s in the word".format(input_letter))
            # deduct a chance
            guesses_left -= 1

        # exit if correct guess
        if current_guess == secret_word:
            break


    print_exit_msg(current_guess, secret_word)


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game from a large list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    f = open(LEXICON_FILE, "r")
    words = f.read().splitlines()
    return random.choice(words)

def update_word(current_guess, input_letter, ind_letter_in_word):
    """
    Strings -> string
    inserts a certain letter in certain indexes in a word
    Input:  current_guess: how much of current word is guessed as displayed in status
            input_letter: inputted letter
            ind_letter_in_word: index where input letters can be found in secret word
    Output: (str) New current_guess with input_letter inserted in the right places
    """
    tmp_list = list(current_guess)
    for i in ind_letter_in_word:
        tmp_list[i] = input_letter.upper()
    return ''.join(tmp_list)

def print_status(current_guess, guesses_left):
    """
    string and integer -> string
    prints current status (how the guessed word looks, chances left) of the game
    """

    print("The word now looks like this: " + current_guess)
    print("You have {} guesses left".format(guesses_left))


def indexes(secret_word, input_letter):
    """
    Strings -> enumerated integer(s)
    (when converted into a list) gives indexes of all locations where a certain letter appears in a word
    """
    for i, x in enumerate(secret_word.lower()):
        if x == input_letter.lower():
            yield i

def print_exit_msg(current_guess, secret_word):
    """
    Str -> str
    prints exit message based on final answer
    """
    if current_guess == secret_word:
        print("Congratulations, the word is: {}".format(secret_word))
    else:
        print("Sorry, you lost. The secret word was: {}".format(secret_word))



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
