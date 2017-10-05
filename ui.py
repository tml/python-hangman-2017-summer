from terminaltables import SingleTable


def render(object, **kw):
    if object == 'gallows':
        render_gallows(**kw)
    if object == 'bank':
        render_bank(**kw)
    if object == 'game_state':
        render_game_state(**kw)


def render_gallows(parts=0, **kw):
    BODY = [
        [' '] * 4, # 0 parts
        ['o'] + [' ']*3,  # 1 part: the head
        ['o', '|'] + [' '] * 2,
        ['o', '\|'] + [' '] * 2,
        ['o', '\|/'] + [' '] * 2,
        ['o', '\|/', '|', ' '],
        ['o', '\|/', '|', '/ '],
        ['o', '\|/', '|', '/ \\'],
    ]
    print("""
          ______
          |    |
          {:>1}    |
         {:^3}   |
          {}    |
         {:^3}   |
               |
           ---------
    """.format(*BODY[parts]))


def render_bank(letters=[], **kw):
    sz = 6  # Size of table
    if not any(letters):
        let = [' ']
    else:
        let = sorted(list(letters))
    table = SingleTable([let[i:i + sz] for i in range(0, len(let), sz)],
                        'Incorrect Guesses')
    table.inner_heading_row_border = False
    table.inner_row_border = True
    table.justify_columns = {idx: val for idx, val in
                             enumerate(['center'] * sz)}
    print("\n{}".format(table.table))


def render_game_state(word="", found=[], **kw):
    for letter in word:
        if letter in found:
            print(letter, end='')
        else:
            print(' _ ', end='')
