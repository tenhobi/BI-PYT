#!/usr/bin/env python3
from os import get_terminal_size
from random import random

cols, rows = get_terminal_size()

board = [[0] * cols for i in range(rows)]

for y in range(1, rows - 1):
    for x in range(1, cols - 1):
        if random() < 0.3:
            board[y][x] = 1

while True:
    for y in range(1, rows - 1):
        for x in range(1, cols - 1):
            print('\033[' + str(y) + ';' + str(x) + 'H'
                  + ('\x1b[7;32m \x1b[0m' if board[y][x] else '\x1b[7;39m \x1b[0m'), end='')

    tmp = [[0] * cols for _ in range(rows)]

    for y in range(1, rows - 1):
        for x in range(1, cols - 1):
            countOfLivingNeighbor = (
                board[y - 1][x - 1] +
                board[y - 1][x] +
                board[y - 1][x + 1] +
                board[y][x - 1] +
                board[y][x + 1] +
                board[y + 1][x - 1] +
                board[y + 1][x] +
                board[y + 1][x + 1]
            )
            cell = board[y][x]
            if cell == 1:
                if 2 <= countOfLivingNeighbor <= 3:
                    tmp[y][x] = 1
            else:
                if countOfLivingNeighbor == 3:
                    tmp[y][x] = 1
    board = tmp
