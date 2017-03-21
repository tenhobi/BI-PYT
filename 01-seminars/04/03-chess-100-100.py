#!/usr/bin/env python3

SIZE = 100

with open('03-output.pbm', 'wb') as f:
    f.write(b'P4\n100 100\n')
    for i in range(SIZE):
        counter = 0
        xs = b''
        for j in range(SIZE):
            counter += 1
            if (i + j) % 2 == 0:
                xs += b'1'
            else:
                xs += b'0'
            if counter == 8:
                print("_", xs, counter, 8 - ((SIZE * SIZE) % 8))
                f.write(bytes([int(xs, 2)]))
                xs = b''
                counter = 0
        if counter != 0:
            xs += b'0' * (8 - counter)
            f.write(bytes([int(xs, 2)]))
