"""
This is our hangman game
"""

import words
import ui

import random
import sys

difficulty_levels = {
    "easy": {
        'word length': (8, 15),
        'commonality': 1.0,
        'guesses': 7
    },
    "medium": {
        'word length': (5, 12),
        'commonality': 0.6,
        'guesses': 9
    },
    "hard": {
        'word length': (3, 8),
        'commonality': 0.3,
        'guesses': random.randint(4, 6)
    }
}

FOUND_LETTERS = set()
WRONG_LETTERS = set()
DEBUG = False


def main():
    user = input("What is your name? ")
    difficulty = input("How hard of a game would you like? {} ".
                       format(list(difficulty_levels.keys())))

    while difficulty not in difficulty_levels.keys():
        difficulty = input("How hard of a game would you like? {} ".
                           format(list(difficulty_levels.keys())))

    game_loop(user, difficulty)


def init_game(difficulty=None):
    global FOUND_LETTERS, WRONG_LETTERS
    FOUND_LETTERS = set()
    WRONG_LETTERS = set()
    return words.choose(difficulty_levels[difficulty])


def restart_game(word):
    ui.render_gallows(parts=len(WRONG_LETTERS))
    again = input("""The word was "{}". Would you like to play again?"""
                  """ ['n' to exit]: """.format(word))
    if again.lower().strip()[0] == 'n':
        print(
            """Oh…well…*sniff*…gee, that's awkward. """
            """OK…no, no, I'll be fine…it's fine.\n"""
            """I guess…I guess, thanks for playing? *cries softly*\n"""
            """No, no – I'm fine. Have a great day. """
            """Come back again some time when you're not so busy?\n"""
        )
        sys.exit(0)
    init_game()


def game_loop(user, difficulty):
    word = init_game(difficulty)
    guess_count = difficulty_levels[difficulty]['guesses']
    while True:
        if game_won(word, FOUND_LETTERS):
            print("Yay, {}!".format(user))
            restart_game(word)

        if len(WRONG_LETTERS) >= guess_count:
            print("Oh, sad day, {}. You lost!".format(user))
            restart_game(word)

        ui.render(object='gallows', parts=len(WRONG_LETTERS))
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
        if DEBUG:
            print("And congrats, {} is in {}".format(choice, word))
    else:
        WRONG_LETTERS.add(choice)
        if DEBUG:
            print("Failed! {} is not in {}.".format(choice, word))
            print(WRONG_LETTERS)


def validate_letter(letter):
    return (len(letter) == 1) and (letter.isalpha())


def game_won(word, found):
    """
    :param word: the correct word which was chosen by words.choose
    :param found: the set of letters which the user has found
    :return: True or False
    """
    if (set(word).difference(set(found)) == set()):
        return True
    return False


if __name__ == "__main__":
    main()
