#!/usr/bin/env python3

from random import random

all = 512
a = 50
b = 90

with open('05-output.pgm', 'w') as f:
    f.write('P3\n512 400\n255\n')
    for i in range(400):
        a += int(round(random()) * 4 - 2)
        b += int(round(random()) * 6 - 2)

        if a > 512:
            a = 512

        if b > 512:
            b = 512

        f.write(f'125 {a} 100 ' * a)
        f.write(f'{a} 0 {b - a} ' * (b - a))
        f.write(f'{b} 219 178 ' * (all - b))
        f.write('\n')
