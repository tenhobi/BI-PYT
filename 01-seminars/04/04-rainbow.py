#!/usr/bin/env python3

xs = []
for i in range(256):
    xs.append(str(i) + ' 0 0')

tam, zpatky = ' '.join(xs), ' '.join(xs[::-1])

with open('04-output.pgm', 'w') as f:
    f.write('P3\n512 400\n255\n')
    for i in range(400):
        f.write(tam + ' ')
        f.write(zpatky + ' ')
        f.write('\n')
