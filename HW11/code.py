from ulab import numpy as np

n = 1024
dt = 0.001 # 1000 Hz
sum_sin = np.zeros(n)

for i in range(n):
    t = dt*i
    sin1 = np.sin(2 * np.pi * 50 * t)
    sin2 = 1 * np.sin(2 * np.pi * 20 * t)
    sin3 = 1 * np.sin(2 * np.pi * 350 * t)
    sum_sin[i] = sin1 + sin2 + sin3
    #print("("+str(sum_sin[i])+",)")

k = np.arange(n)
T = dt * n
freq = k / T
freq = freq[:int(n/2)]
Y = np.fft.fft(sum_sin)[0]/n
Y = Y[:int(n/2)]

for i in range(len(freq)):
    #print("(" + str(freq[i]) + ", " + str(Y[i]) + ",)")
    print(str(freq[i]) + "," + str(abs(Y[i])))
