from __future__ import annotations

import os
import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else 'example_input'


INPUT_DIR = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__),
    ),
    input_file,
)


lines: list[str]
with open(INPUT_DIR, 'r+') as f:
    lines = f.read().splitlines()


result = 0

for line in lines:
    _, rest = line.split(': ')

    deck = rest.split('| ')

    winning = {int(n) for n in deck[0].split(' ') if n}

    drawed = list(int(n) for n in deck[1].split(' ') if n)

    matched = -1
    for card in drawed:
        if card in winning:
            winning.remove(card)
            matched += 1

    if matched > -1:
        result += 2 ** matched

print('Result: ', result)
