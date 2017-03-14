import time
from os import get_terminal_size as gts
import sys

printx = sys.stdout.write
flushx = sys.stdout.flush

def reset ():
    printx('\033[0m')

def white ():
    printx('\033[43m  ')
    reset()

def black ():
    printx('\033[44m  ')
    reset()

reset()

cols, rows = gts()
cols, rows = cols // 2, rows

for i in range (1, rows - 1):
    for j in range(1, cols):
        if ((i + j) % 2 == 0):
            black()
        else:
            white()
    printx('\n')

flushx()
