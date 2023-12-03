from __future__ import annotations

import os

INPUT_DIR = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__),
    ),
    'input',
)

input: list[str]
with open(INPUT_DIR, 'r+') as f:
    input = f.read().splitlines()


result = 0
for i in input:
    # keep only digits from i and add to result
    d = ''.join(filter(str.isdigit, i))
    result += int(d[0] + d[-1])

print('Result:', result)
