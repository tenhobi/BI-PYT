#!/usr/bin/env python3
from struct import unpack
import zlib


class NotPNGError(Exception):
    pass


class CRCError(Exception):
    pass


def get_next_chunk(f):
    # DATA LENGTH
    while True:
        data_len = f.read(4)
        #	print(data_len)
        data_len = unpack('>I', data_len)[0]

        # HEADER
        header = f.read(4)

        # DATA
        data = f.read(data_len)

        # CRC
        crc = f.read(4)
        # if zlib.crc32(header + data) != crc:
        #	raise CRCError( ' in chunk ' + header.decode('ascii'))
        # RETURN
        yield header.decode('ascii'), data

        # EOF?
        if header == b'IEND':
            return


# br ke cteni
img = {}
with open('sachovnice.png', 'br') as f:
    # bez parametru nacte cely soubor
    # s parametrem binarne odpovida poctu bytu
    png_header = f.read(8)

    # test na PNG:
    if png_header != b'\x89PNG\r\n\x1a\n':
        raise NotPNGError
    # je to (asi ) PNG, tak ho zkusime nacist

    '''	
        for chunk in get_next_chunk(f):
            print(chunk)
    '''
    for header, data in get_next_chunk(f):
        img[header] = data
# IHDR
ihdr = img['IHDR']
width, height = unpack('>I', ihdr[:4])[0], unpack('>I', ihdr[4:8])[0]
print(width, height)
# asssert ihdr[8:] == b'\x08\x02\x00\x00\x00'

# IDAT
pnm_data = b''
idat = img['IDAT']
idat = zlib.decompress(idat)
line_len = 1 + width * 3
for i in range(0, len(idat), line_len):
    line = idat[i:i + line_len]
    print(line)
    filter = line[0]
    if filter == 0:
        # fajn
        pnm_data += line[1:]
    for j in range(width):
        idx = 1 + 3 * j
        print('\t', line[idx:idx + 3])

# PNM P6
with open('sachovnice.pnm', 'bw') as f:
    f.write(b'P6\n' + str(width).encode('ascii') + b' ' + str(height).encode('ascii') + b'\n255\n')
    f.write(pnm_data)



