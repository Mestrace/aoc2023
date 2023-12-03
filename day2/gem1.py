# The Elf would first like to know which games would have been
# possible if the bag contained only 12 red cubes, 13 green
# cubes, and 14 blue cubes?
from __future__ import annotations

import os
from collections import defaultdict

INPUT_DIR = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__),
    ),
    'input',
)

# parse input
games = []
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

expected = {'red': 12, 'green': 13, 'blue': 14}
result = 0
for i, game in enumerate(games):
    if len(game.keys()) <= len(expected.keys()) and all(
        game[key] <= expected[key] for key in expected.keys()
    ):
        print(i + 1, game)
        result += i + 1
print('result: ', result)
