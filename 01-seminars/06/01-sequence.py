#!/usr/bin/env python3
import gzip

with gzip.open('yersinia_pseudotuberculosis.fasta.gz', mode='tr') as f:
    sequence = ''.join(f.read().strip().split('\n')[1:])

# print(data[:10])
# print(data[-2:])

print(len(sequence))
print((sequence.count('C') + sequence.count('G')) / len(sequence))
