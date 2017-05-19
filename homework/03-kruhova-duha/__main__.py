#!/usr/bin/env python3
import colorsys
import math

WIDTH = 200
RADIUS = WIDTH / 2

NUMBER_OF_SAMPLES = 360
HSV_tuples = [x * 1.0 / NUMBER_OF_SAMPLES for x in range(NUMBER_OF_SAMPLES)]


def get_angle(target):
    angle = math.degrees(math.atan2(target[0] - RADIUS, target[1] - RADIUS))

    if angle < 0:
        angle += 360

    return int(angle)


def get_distance(target):
    return math.sqrt((target[0] - RADIUS) ** 2 + (target[1] - RADIUS) ** 2)


image_data = b''

for y in range(0, WIDTH):
    for x in range(0, WIDTH):
        # pixel for rainbow
        if get_distance([y, x]) <= RADIUS:
            pixel = list(colorsys.hsv_to_rgb(HSV_tuples[get_angle([y, x])], 1, 1))
            # percentage value 0.0-1.0 to range value 0-255
            pixel[0] = int(pixel[0] * 255)
            pixel[1] = int(pixel[1] * 255)
            pixel[2] = int(pixel[2] * 255)
            image_data += bytes(pixel)
        # pixel for background
        else:
            image_data += bytes([255] * 3)

with open('rainbow-circle.pnm', 'bw') as f:
    f.write(b'P6\n' + str(WIDTH).encode('ascii') + b' ' + str(WIDTH).encode('ascii') + b'\n255\n')
    f.write(image_data)
