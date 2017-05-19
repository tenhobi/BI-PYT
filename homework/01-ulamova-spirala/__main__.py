#!/usr/bin/env python3
import math
import os
import time

NUM_SIZE = 5

# clear window
print('\033[2J')

# get dimension and center
cols, rows = os.get_terminal_size()
x = cols // 2
y = rows // 2
print(f'\033[{y};{x}H', end='', flush=True)


# returns True if number is prime
def is_prime(number):
    if number > 1:
        if number == 2:
            return True

        if number % 2 == 0:
            return False

        for i in range(3, int(math.sqrt(number) + 1), 2):
            if number % i == 0:
                return False

        return True
    return False


# generator of direction for ulam spiral
def ulam_direction_generator():
    direction = 0
    while True:
        yield direction
        direction = (direction + 1) % 4
        yield direction
        direction = (direction + 1) % 4


# generator of distance for ulam spiral
def ulam_distance_generator():
    distance = 1
    while True:
        yield distance
        yield distance
        distance += 1


direction_generator = ulam_direction_generator()
distance_generator = ulam_distance_generator()

number = 1

while True:
    for _ in range(0, 2):
        distance = next(distance_generator)
        direction = next(direction_generator)
        for _ in range(0, distance):
            modifiers = ""
            if is_prime(number):
                modifiers += "\033[1;31m"

            print(f'\033[{y};{x}H{modifiers}{str(number).rjust(NUM_SIZE)}\033[0m', end='', flush=True)

            number += 1

            if direction == 0:
                x += NUM_SIZE
            elif direction == 1:
                y -= 1
            elif direction == 2:
                x -= NUM_SIZE
            elif direction == 3:
                y += 1
            else:
                raise ValueError("Impossible direction value.")

    # no more space in window
    if y <= 1 or x <= 1 or y >= rows or x >= cols:
        break

print(f'\033[0m\033[{rows};0H', end='', flush=True)
