def render(object, **kw):
    if object == 'gallows':
        render_gallows(**kw)
    if object == 'bank':
        render_bank(**kw)
    if object == 'game_state':
        render_game_state(**kw)

def render_gallows(parts=0, **kw):
    print("""
        ______
        |    |
        O    |
        |    |
        |    |
        /    |
             |
         ---------
    """)

def render_bank(letters=[], **kw):
    print("""
_________________________
|                       |
|                       |
|                       |
-------------------------
        """)

def render_game_state(word="", found=[], **kw):
    for letter in word:
        if letter in found:
            print(letter, end='')
        else:
            print(' _ ', end='')