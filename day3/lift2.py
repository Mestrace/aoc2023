from __future__ import annotations

import os

INPUT_DIR = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__),
    ),
    'input',
)


lines: list[str]
with open(INPUT_DIR, 'r+') as f:
    lines = f.read().splitlines()

M = len(lines)
N = len(lines[0])

ufid = 0
uf = [-1] * (M * N)
mapping: dict[int, int] = dict()


def _union(points: list[tuple[int, int]], value: int):
    global ufid
    for x, y in points:
        if uf[x * N + y] == -1:
            uf[x * N + y] = ufid
        else:
            raise Exception('Should not contain duplicate', x, y)

    mapping[ufid] = value
    ufid += 1


def _retrieve_id(x, y):
    return uf[x * N + y]


for row in range(len(lines)):
    stack = []
    num = 0
    for col in range(len(lines[row])):
        if lines[row][col].isdigit():
            stack.append((row, col))
            num = num * 10 + int(lines[row][col])
        elif len(stack) > 0:
            _union(stack, num)
            # clear
            stack = []
            num = 0
    if len(stack) > 0:
        _union(stack, num)

result = 0


# assuming there are only 2 gears present
def _compute_gear_ratio(x, y):
    # Directions for the 8 adjacent cells
    DIR = [
        (-1, -1), (-1, 0), (-1, 1), (0, -1),
        (0, 1), (1, -1), (1, 0), (1, 1),
    ]

    mult = set()

    for dx, dy in DIR:
        nx, ny = x + dx, y + dy
        if not 0 <= nx < M or not 0 <= ny < N:
            continue
        if lines[nx][ny].isdigit():
            _id = _retrieve_id(nx, ny)
            if _id != -1:
                mult.add(_id)

    if len(mult) == 2:
        _id1, _id2 = mult
        return mapping[_id1] * mapping[_id2]
    elif len(mult) > 2:
        raise Exception(
            'Asumption broken: should only have 2 gears around', mult,
        )
    return 0


result = 0
for row in range(len(lines)):
    for col in range(len(lines[row])):
        if lines[row][col] == '*':
            result += _compute_gear_ratio(row, col)

print('Result:', result)
