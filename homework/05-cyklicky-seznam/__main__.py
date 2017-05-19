#!/usr/bin/env python3
from cyclic_list import CyclicList

xs = CyclicList(range(10))

print(1, "...", xs)
print(2, "...", len(xs))
print(3, "...", xs[9])
print(4, "...", xs[10])
print(5, "...", xs[8:])
print(6, "...", xs[18:])
print(7, "...", xs[-10])
print(8, "...", xs[-11])
print(9, "...", xs[::3])
print(10, "...", xs[::-3])

for x in xs:
    print(x)
