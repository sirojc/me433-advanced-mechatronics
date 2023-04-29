import matplotlib.pyplot as plt
import numpy as np
import csv


def filters(name, n_avg, A, B, w):
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
    movavg = []
    tavg = []
    for i in range(0, len(meas)-n_avg):
        movavg.append(np.mean(meas[i:i+n_avg]))
        tavg.append(np.mean(t[i:i+n_avg]))

    fig2, ax1 = plt.subplots()
    ax1.plot(t,meas,'k')
    ax1.plot(tavg, movavg, 'r')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Amplitude')
    ax1.set_title('Mov Avg Sig' + name + ' (n=' + str(n_avg) + ')')
    plt.savefig('plots/Sig' + name + '_movavg.png')

    ### 6 IIR ###

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
    fir = []
    l = len(w)
    w = np.array(w)
    meas = np.array(meas)
    for i in range(len(meas)-l):
        fir.append(np.dot(w.T,meas[i:i+l])/l) #TODO
    t_fir = t[l:]

    fig4, ax1 = plt.subplots()
    ax1.plot(t,meas,'k')
    ax1.plot(t_fir, fir, 'r')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Amplitude')
    ax1.set_title('FIR Sig' + name + 'n = ' + str(l)) #TODO
    plt.savefig('plots/Sig' + name + '_fir.png')


name = 'A'
n_avg = 400 # mov avg
A = 0.9965 # IIR
B = 0.0035 # IIR
w = [1,1,1,1,1,1,1,1,1,1]
filters(name, n_avg, A, B, w)

name = 'B'
n_avg = 100 # mov avg
A = 0.985 # IIR
B = 0.015 # IIR
filters(name, n_avg, A, B, w)

name = 'C'
n_avg = 1 # mov avg
A = 0 # IIR
B = 1 # IIR
filters(name, n_avg, A, B, w)

name = 'D'
n_avg = 45 # mov avg
A = 0.94 # IIR
B = 0.06 # IIR
filters(name, n_avg, A, B, w)



