"""
This is our hangman game
"""

import words
import ui

import random
import sys

difficulty_levels = {
    "easy": {
        'word length': (3, 8),
        'commonality': 1.0,
        'guesses': 15
    },
    "medium": {
        'word length': (8, 15),
        'commonality': 1.0,
        'guesses': 9
    },
    "hard": {
        'word length': (15, 20),
        'commonality': 1.0,
        'guesses': random.randint(4, 6)
    }
}

FOUND_LETTERS = set()
WRONG_LETTERS = set()


def main():
    user = input("What is your name? ")
    difficulty = input("How hard of a game would you like? {} ".
                       format(list(difficulty_levels.keys())))

    while difficulty not in difficulty_levels.keys():
        difficulty = input("How hard of a game would you like? {} ".
                           format(list(difficulty_levels.keys())))

    our_word = words.choose(difficulty_levels[difficulty]['word length'])
    game_loop(user, our_word, difficulty_levels[difficulty]['guesses'])


def game_loop(user, word, guess_count, parts=None):
    while True:
        if game_won(word, FOUND_LETTERS):
            print("Yay, {}!".format(user))
            sys.exit()

        if len(WRONG_LETTERS) >= guess_count:
            print("Oh, sad day, {}. You lost!".format(user))
            sys.exit()

        ui.render(object='gallows', parts=0)
        ui.render(object='game_state', word=word, found=FOUND_LETTERS)
        ui.render(object='bank', letters=WRONG_LETTERS)
        guess_letter(word)


def guess_letter(word):
    choice = input("Please enter a letter: ").lower()
    if choice == "quit":
        print("OK. Thanks for playing!")
        sys.exit(0)
    if validate_letter(choice) is False:
        print("That's not a valid guess; please choose a single letter.")
        return
    print("You guessed {}".format(choice))
    if choice in word:
        FOUND_LETTERS.add(choice)
        print("And congrats, {} is in {}".format(choice, word))
    else:
        WRONG_LETTERS.add(choice)
        print("Failed! {} is not in {}.".format(choice, word))
        print(WRONG_LETTERS)


def validate_letter(letter):
    return (len(letter) == 1) and (letter.isalpha())


def game_won(word, found):
    for letter in word:
        if letter not in found:
            return False


if __name__ == "__main__":
    main()
