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


N = len(lines)
deck_count = []

for line in lines:
    _, rest = line.split(': ')

    deck = rest.split('| ')

    winning = {int(n) for n in deck[0].split(' ') if n}

    drawed = list(int(n) for n in deck[1].split(' ') if n)

    matched = 0
    for card in drawed:
        if card in winning:
            winning.remove(card)
            matched += 1

    deck_count.append(matched)


counter = [0] * len(deck_count)
counter[0] = 1

result = 0
accumulate = 0
for i in range(N):
    accumulate += counter[i]

    print('Card', i+1, accumulate)

    result += accumulate

    if i + 1 < N:
        counter[i + 1] += accumulate

    if i + deck_count[i] + 1 < N:
        counter[i + deck_count[i] + 1] -= accumulate


print('Result: ', result)
