#!/usr/bin/env python3
import gzip
import matplotlib.pyplot as plt
import random

with gzip.open('yersinia_pseudotuberculosis.fasta.gz', mode='tr') as f:
    sequence = ''.join(f.read().strip().split('\n')[1:])

# print(len(sequence))
# print(((sequence.count('C') + sequence.count('G')) / len(sequence)) * 100)

average = (sequence.count('G') + sequence.count('C')) / len(sequence)

STEP = 100000

sequence = list(sequence)

data = []
for i in range(0, len(sequence), STEP):
    cut = sequence[i:i + STEP]
    # print(len(cut))
    print((cut.count('G') + cut.count('C')) / STEP)
    data.append((cut.count('G') + cut.count('C')) / STEP)

plt.plot([i for i in range(0, len(sequence), STEP)], data, 'b+', label='průměr přes sliding window')
plt.plot([0, 5000000], [average, average], 'r-', label='celkový průměr')

random.shuffle(sequence)
data = []
for i in range(0, len(sequence), STEP):
    cut = sequence[i:i + STEP]
    # print(len(cut))
    print((cut.count('G') + cut.count('C')) / STEP)
    data.append((cut.count('G') + cut.count('C')) / STEP)

print(data)

plt.plot([i for i in range(0, len(sequence), STEP)], data, 'g+', label='průměr přes sliding window v náhodné sekvenci')


plt.xlabel('pořadí v sekvenci')
plt.ylabel('obsah GC')
plt.title('Procentuální zastoupení GC v genomu')
plt.legend()

plt.show()
