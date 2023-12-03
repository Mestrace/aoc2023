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


def _check(points):
    # Directions for the 8 adjacent cells
    DIR = [
        (-1, -1), (-1, 0), (-1, 1), (0, -1),
        (0, 1), (1, -1), (1, 0), (1, 1),
    ]
    visited = set(points)

    for x, y in points:
        for dx, dy in DIR:
            nx, ny = x + dx, y + dy
            if not 0 <= nx < M or not 0 <= ny < N:
                continue
            if (nx, ny) in visited:
                continue
            visited.add((nx, ny))
            if not lines[nx][ny].isalnum() and lines[nx][ny] != '.':
                # print("checked", nx, ny, lines[nx][ny])
                return True
    return False


result = 0
for row in range(len(lines)):
    stack = []
    num = 0
    for col in range(len(lines[row])):
        if lines[row][col].isdigit():
            stack.append((row, col))
            num = num * 10 + int(lines[row][col])
        elif len(stack) > 0:
            if _check(stack):
                result += num

            # clear
            stack = []
            num = 0
    if len(stack) > 0:
        if _check(stack):
            result += num

print('Result:', result)
