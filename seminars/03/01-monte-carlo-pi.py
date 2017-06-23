#!/usr/bin/env python3
from math import sqrt
from random import random

inside, outside = 0, 0

for i in range(100000):
    x, y = random(), random()
    if sqrt(x ** 2 + y ** 2) <= 1:
        inside += 1
    else:
        outside += 1

print(4 * inside / (inside + outside))
