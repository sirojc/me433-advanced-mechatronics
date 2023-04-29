import matplotlib.pyplot as plt
import numpy as np
import csv

names = ['A', 'B', 'C', 'D']
for name in names:
    t = []
    meas = []

    with open('data/Sig' + name + '.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            t.append(float(row[0]))
            meas.append(float(row[1]))

    Ts = t[-1]/(len(t)-1)
    Fs = 1/Ts

    ### 4 FFT ###
    ts = t
    n = len(meas) # length of the signal
    k = np.arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(int(n/2))] # one side frequency range
    Y = np.fft.fft(meas)/n # fft computing and normalization
    Y = Y[range(int(n/2))]

    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot(t,meas,'b')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Amplitude')
    ax2.loglog(frq,abs(Y),'b') # plotting the fft
    ax2.set_xlabel('Freq (Hz)')
    ax2.set_ylabel('|Y(freq)|')
    ax1.set_title('Sig' + name)
    plt.savefig('plots/Sig' + name + '_fft.png')

    ### 5 Moving Average ###
    n = 50
    movavg = []
    tavg = []
    for i in range(0, len(meas)-n):
        movavg.append(np.mean(meas[i:i+n]))
        tavg.append(np.mean(t[i:i+n]))

    fig2, ax1 = plt.subplots()
    ax1.plot(t,meas,'k')
    ax1.plot(tavg, movavg, 'r')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Amplitude')
    ax1.set_title('Mov Avg Sig' + name + ' (n=' + str(n) + ')')
    plt.savefig('plots/Sig' + name + '_movavg.png')

    ### 6 IIR ###
    A = 0.99
    B = 0.01

    iir = [meas[0]]
    for i in range(1, len(meas)):
        iir.append(A * iir[i-1] + B * meas[i])

    fig3, ax1 = plt.subplots()
    ax1.plot(t,meas,'k')
    ax1.plot(t, iir, 'r')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Amplitude')
    ax1.set_title('IIR Sig' + name + ', A =' + str(A) + ', B =' + str(B))
    plt.savefig('plots/Sig' + name + '_iir.png')

    ### 7 FIR ###



