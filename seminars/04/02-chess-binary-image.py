#!/usr/bin/env python3

with open('02-output.pbm', 'wb') as f:
    f.write(b'P4\n8 8\n')
    for i in range(8):
        xs = ''
        for j in range(8):
            if (i + j) % 2 == 0:
                xs += '1'
            else:
                xs += '0'
        f.write(bytes([int(xs, 2)]))
