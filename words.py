"""
    Pick a word from /usr/share/dict/words
"""

import subprocess
import random


def choose(difficulty):
    (min, max) = difficulty['word length']
    file = 'data/easy.words'
    if difficulty['commonality'] < 0.5:
        file = 'data/hard.words'
    cmd = """/usr/bin/grep -E '^.{{{},{}}}$' {}""".format(min, max, file)
    obj = subprocess.run(cmd,
                         shell=True,
                         stdout=subprocess.PIPE)
    result = obj.stdout.decode('utf-8').strip().split("\n")
    return random.choice(result)


if __name__ == "__main__":
    choose((3, 8))
