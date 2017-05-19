#!/usr/bin/env python3
from random import randint
import os
from time import sleep

# clear window
print('\033[2J')

# get dimension and center
cols, rows = os.get_terminal_size()
x = cols // 2
y = rows // 2
print(f'\033[{y};{x}H', end='', flush=True)

matrix = [[0] * (cols + 1) for i in range(rows + 1)]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

while True:
    direction = randint(0, 7)

    # cycle through steps in the direction
    for _ in range(0, randint(1, 5)):
        x += directions[direction][0]
        y += directions[direction][1]

        # change visual of current cell
        if matrix[y][x] < 7:
            matrix[y][x] += 1

        print(f'\033[{y};{x}H\033[4{matrix[y][x]}m \033[0m', end='', flush=True)

        sleep(0.02)

        if not ((1 < y < rows) and (1 < x < cols)):
            break

    if not ((1 < y < rows) and (1 < x < cols)):
        break

print(f'\033[0m\033[{rows};0H', end='', flush=True)
