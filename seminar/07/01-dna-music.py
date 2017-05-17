#!/usr/bin/env python3
import gzip
from .slovnik import *

dictionary = {}

with open('aminokyseliny_abc.csv') as file:
    for line in file:
        data = line.strip().split('\t')
        akord = data[-1]

        for kodon in data[3].split(', '):
            dictionary[kodon] = akord

with open('slovnik.py', 'w') as file:
    file.write('#!/usr/bin/env python3\n\n')
    file.write('tabulka = {\n')

    for k, v in sorted(dictionary.items()):
        file.write(' ' * 4 + '"' + k.replace('U', 'T') + '": "' + v + '",\n')

    file.write('}\n')

with gzip.open('../06/yersinia_pseudotuberculosis.fasta.gz', mode='tr') as f:
    sequence = ''.join(f.read().strip().split('\n')[1:])

with open('hudba.abc', 'w') as f:
    f.write('X:1\n')
    f.write('K:C\n')

    for i in range(0, len(sequence), 3):
        kodon = sequence[i:i + 3]
        f.write(tabulka.get(kodon, ''))
