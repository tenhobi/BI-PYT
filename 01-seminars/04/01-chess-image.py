#!/usr/bin/env python3

with open('01-output.pbm', 'w') as f:
    f.write('P1\n8 8\n')
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                f.write('1 ')
            else:
                f.write('0 ')
        f.write('\n')
