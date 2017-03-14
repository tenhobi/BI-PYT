#!/usr/bin/env python3
import time
from os import get_terminal_size as gts
import sys

printx = sys.stdout.write
flushx = sys.stdout.flush

def reset ():
    printx('\033[0m')

def ball (x, y):
    printx(f'\033[{y-vectorY};{x-vectorX}H ') # delete last ball
    printx(f'\033[{y};{x}Ho') # draw new ball
    flushx()

def drawEdges (width, height, edge):
    for x in range(edge, width - edge + 2):
        for y in range(edge, height - edge + 2):
            if (y == edge) or (x == edge) or (x == width - edge + 1) or (y == height - edge + 1):
                printx(f'\033[{y};{x}H-')
    flushx()
    pass

reset()

maxX, maxY = gts()
y = 23
x = 10

edge = 5

drawEdges(maxX, maxY, edge)

vectorX = 1
vectorY = -1

while True:
    ball(x, y)

    if (x == maxX - edge) or (x == 1 + edge):
        vectorX = -vectorX

    if (y == maxY - edge) or (y == 1 + edge):
        vectorY = -vectorY

    x += vectorX
    y += vectorY
    time.sleep(0.05)
