import matplotlib.pyplot as plt
import numpy as np
import csv

freq = []
amp = []

with open('output.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        freq.append(float(row[0]))
        amp.append(float(row[1]))

#print(freq)
#print(amp)

fig, ax = plt.subplots()
ax.plot(freq, amp,'b')
ax.set_xlabel('Freq (Hz)')
ax.set_ylabel('|Y(freq)|')
ax.set_title('FFT of 3 superimposed sine waves')
fig.tight_layout()
plt.savefig('fft_3_sin.png')
plt.show()


