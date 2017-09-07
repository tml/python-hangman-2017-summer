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


def main():
    parts = 0
    guess_count = 0
    found = []
    bank = []

    user = input("What is your name? ")
    difficulty = input("How hard of a game would you like? {} ".
                       format(list(difficulty_levels.keys())))

    while difficulty not in difficulty_levels.keys():
        difficulty = input("How hard of a game would you like? {} ".
                           format(list(difficulty_levels.keys())))

    our_word = 'mississippi'

    found = ['i', 's', 'p']
    bank = ['e', 'a', 't', 'o', 'h']

    # our_word = words.choose(length=
    # difficulty_levels[difficulty]['word length'])
    # ui.render(object='gallows', parts=0)
    # ui.render(object='game_state', word=our_word, found=found)
    # ui.render(object='bank', letters=bank)


def game_loop(word, found, bank, guess_count, parts):
    while True:
        if game_won(word, found):
            print("Yay!")
            sys.exit()
        else:
            ui.render(object='gallows', parts=0)
            ui.render(object='game_state', word=word, found=found)
            ui.render(object='bank', letters=bank)


def game_won(word, found):
    for letter in word:
        if letter not in found:
            return False


if __name__ == "__main__":
    main()
