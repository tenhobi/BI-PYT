#!/usr/bin/env python3
from os import get_terminal_size
import numpy as np

cols, rows = get_terminal_size()

display = np.zeros([rows, cols], dtype=np.uint8)

board = display[1:-1, 1:-1]
board[...] = np.random.randint(0, 2, size=board.shape)
Y, X = board.shape

while True:
    for y in range(Y):
        for x in range(X):
            print('\033[' + str(y) + ';' + str(x) + 'H'
                  + ('\x1b[7;32m \x1b[0m' if board[y, x] else '\x1b[7;39m \x1b[0m'), end='')
    o = np.zeros(board.shape, dtype=np.uint8)
    o[...] = (
        display[0:-2, 0:-2] + display[0:-2, 1:-1] + display[0:-2, 2:] +
        display[1:-1, 0:-2] + display[1:-1, 2:] +
        display[2:, 0:-2] + display[2:, 1:-1] + display[2:, 2:]
    )
    board[...] = ((o == 3) | ((board == 1) & (o == 2)))
