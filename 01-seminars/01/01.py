#!/usr/bin/env python3
import time
from os import get_terminal_size as gts
import sys

printx = sys.stdout.write
flushx = sys.stdout.flush

cols, rows = gts()
cols, rows = cols // 2, rows // 2

printx('\033[2J')
printx(f'\033[{rows};{cols}H')
printx('\033[1;35;40m')

while True:
    for i in range(1, 61):
        printx(f"{i:2}")
        flushx()
        time.sleep(0.1)
        printx('\b\b')
