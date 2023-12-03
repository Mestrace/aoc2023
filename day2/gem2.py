# As you continue your walk, the Elf poses a second question: in each game you
# played, what is the fewest number of cubes of each color that could have
# been in the bag to make the game possible?
from __future__ import annotations

import os
from collections import defaultdict
from functools import reduce

INPUT_DIR = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__),
    ),
    'input',
)

# parse input
games: list[dict[str, int]] = []
f = None
with open(INPUT_DIR, 'r+') as f:
    lines = f.read().splitlines()
    for line in lines:
        _, rest = line.split(': ')
        d: dict[str, int] = defaultdict(int)
        for play in rest.split('; '):
            for gem in play.split(', '):
                num, color = gem.split(' ')
                d[color] = max(d[color], int(num))
        print(d)
        games.append(d)

minimum: dict[str, int] = defaultdict(int)
result = 0
for i, game in enumerate(games):
    result += reduce(lambda a, b: a * b, game.values())

print('result:', result)
