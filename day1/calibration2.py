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


THREE_LETTER_NUMBER = {'one': 1, 'two': 2, 'six': 6}

FOUR_LETTER_NUMBER = {'four': 4, 'five': 5, 'nine': 9}

FIVE_LETTER_NUMBER = {'three': 3, 'seven': 7, 'eight': 8}


# function that reads letter and convert 1-9 in english to number
# 5eight97nine -> 5 8(eight) 9 7 9(nine)
# 4sixfour4nppgsr36one3 -> 4 6(six) 4(four) 4 3 6 1(one) 3
def _convert(s: str):
    for i in range(len(s)):
        if s[i].isdigit():
            yield int(s[i])
        elif s[i: i + 3] in THREE_LETTER_NUMBER:
            yield THREE_LETTER_NUMBER[s[i: i + 3]]
        elif s[i: i + 4] in FOUR_LETTER_NUMBER:
            yield FOUR_LETTER_NUMBER[s[i: i + 4]]
        elif s[i: i + 5] in FIVE_LETTER_NUMBER:
            yield FIVE_LETTER_NUMBER[s[i: i + 5]]


# input = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen""".split(
#     "\n"
# )

result = 0
for i in input:
    # keep only digits from i and add to result
    d = list(_convert(i))
    result += d[0] * 10 + d[-1]

print('Result:', result)
