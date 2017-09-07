"""
    Pick a word from /usr/share/dict/words
"""

import subprocess
from sys import exit
import random

def choose(difficulty):
    (min, max) = difficulty
    cmd = "/usr/bin/grep -E '^.{{{},{}}}$' /usr/share/dict/words".format(min, max)
    obj = subprocess.run(cmd,
                         shell=True,
                         stdout=subprocess.PIPE)
    result = obj.stdout.decode('utf-8').strip().split("\n")
    return random.choice(result)