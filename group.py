import words
import ui
import random
import sys

difficulty_levels = {
    "easy": {
        'word length': (3,8),
        'commonality': 1.0,
        'guesses': 15
    },
    "medium": {
        'word length': (8, 15),
        'commonality': 1.0,
        'guesses': 9
    },
    "hard": {
        'word length': (15,20),
        'commonality': 1.0,
        'guesses': random.randint(4,6)
    }
}


def main():
    parts = 0
    guess_count = 0
    found = []
    bank = []

    user = input("What is your name? ")
    difficulty = input("How hard of a game would you like? {} ".format(list(difficulty_levels.keys())))

    # our_word = words.choose(length=difficulty_levels[difficulty]['word length'])
    # ui.render(object='gallows', parts=0)
    # ui.render(object='game_state', word=our_word, found=found)
    # ui.render(object='bank', letters=bank)
