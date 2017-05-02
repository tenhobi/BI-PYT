#!/usr/bin/env python3
from pprint import pprint
from random import random

N = 100  # number of available steps
K = range(1, 101, 10)  # number of steps away from a pub
P = [x / 10 for x in range(1, 10)]  # chance to get to a pub


def nh(N, k, P):
    steps = 0  # number of steps
    while 0 < k < N:
        steps += 1
        if random() >= P:  # to home
            k -= 1
        else:  # to pub
            k += 1
    return 'H' if k == 0 else 'P', steps

attempts = {}
for p in P:
    for k in K:
        attempts[(k, p)] = nh(N, k, p)

pprint(attempts)
