import matplotlib.pyplot as plt
import numpy as np
import csv

w1 = [
    0.001867519746044820,
    0.002275293677911463,
    0.002692845467883248,
    0.003119400211540369,
    0.003554151391578438,
    0.003996262853518041,
    0.004444870878876082,
    0.004899086349965267,
    0.005357997000181999,
    0.005820669743355830,
    0.006286153075466025,
    0.006753479541784039,
    0.007221668262275161,
    0.007689727507889525,
    0.008156657320192493,
    0.008621452166627776,
    0.009083103623574271,
    0.009540603079249766,
    0.009992944448431896,
    0.010439126890909214,
    0.010878157525543523,
    0.011309054131818317,
    0.011730847830767882,
    0.012142585737226980,
    0.012543333575412086,
    0.012932178249941664,
    0.013308230364524597,
    0.013670626680692492,
    0.014018532509122373,
    0.014351144026291085,
    0.014667690509420725,
    0.014967436482914990,
    0.015249683769748768,
    0.015513773441556675,
    0.015759087661469738,
    0.015985051414072162,
    0.016191134117190663,
    0.016376851110586923,
    0.016541765016997088,
    0.016685486971350718,
    0.016807677714403370,
    0.016908048547430839,
    0.016986362145057821,
    0.017042433223728004,
    0.017076129063764694,
    0.017087369883420026,
    0.017076129063764694,
    0.017042433223728004,
    0.016986362145057821,
    0.016908048547430839,
    0.016807677714403370,
    0.016685486971350718,
    0.016541765016997088,
    0.016376851110586923,
    0.016191134117190663,
    0.015985051414072162,
    0.015759087661469738,
    0.015513773441556675,
    0.015249683769748768,
    0.014967436482914990,
    0.014667690509420725,
    0.014351144026291085,
    0.014018532509122373,
    0.013670626680692492,
    0.013308230364524597,
    0.012932178249941664,
    0.012543333575412086,
    0.012142585737226980,
    0.011730847830767882,
    0.011309054131818317,
    0.010878157525543523,
    0.010439126890909214,
    0.009992944448431896,
    0.009540603079249766,
    0.009083103623574271,
    0.008621452166627776,
    0.008156657320192493,
    0.007689727507889525,
    0.007221668262275161,
    0.006753479541784039,
    0.006286153075466025,
    0.005820669743355830,
    0.005357997000181999,
    0.004899086349965267,
    0.004444870878876082,
    0.003996262853518041,
    0.003554151391578438,
    0.003119400211540369,
    0.002692845467883248,
    0.002275293677911463,
    0.001867519746044820,
]
w2 = [
    0.000000000000000000,
    -0.000000733187507994,
    -0.000002514832169553,
    -0.000004663189391103,
    -0.000006411912043391,
    -0.000006894650075208,
    -0.000005128921027786,
    0.000000000000000000,
    0.000009754363726571,
    0.000025557561404639,
    0.000049005219802397,
    0.000081872943140811,
    0.000126119913694109,
    0.000183887634646637,
    0.000257493196406908,
    0.000349416569001100,
    0.000462281565774996,
    0.000598830284134460,
    0.000761891003573286,
    0.000954339705406193,
    0.001179055567694072,
    0.001438870977808257,
    0.001736516788789889,
    0.002074563718984522,
    0.002455360952379098,
    0.002880973134926539,
    0.003353117075610483,
    0.003873099546309844,
    0.004441757628542494,
    0.005059403075507749,
    0.005725772142930002,
    0.006439982291319788,
    0.007200497075605886,
    0.008005100416757878,
    0.008850881296018204,
    0.009734229728566586,
    0.010650844663521859,
    0.011595754225546215,
    0.012563348464977427,
    0.013547424523904094,
    0.014541243860821495,
    0.015537600912594417,
    0.016528902315624129,
    0.017507255564510497,
    0.018464565762032634,
    0.019392638914479399,
    0.020283290056267139,
    0.021128454351758700,
    0.021920299223858908,
    0.022651335501065052,
    0.023314525559019444,
    0.023903386460090124,
    0.024412086164923179,
    0.024835531002085399,
    0.025169442733675097,
    0.025410423743004226,
    0.025556009091159522,
    0.025604704437664948,
    0.025556009091159525,
    0.025410423743004226,
    0.025169442733675097,
    0.024835531002085399,
    0.024412086164923172,
    0.023903386460090128,
    0.023314525559019444,
    0.022651335501065056,
    0.021920299223858911,
    0.021128454351758696,
    0.020283290056267146,
    0.019392638914479399,
    0.018464565762032644,
    0.017507255564510504,
    0.016528902315624129,
    0.015537600912594422,
    0.014541243860821501,
    0.013547424523904100,
    0.012563348464977434,
    0.011595754225546215,
    0.010650844663521864,
    0.009734229728566589,
    0.008850881296018210,
    0.008005100416757878,
    0.007200497075605891,
    0.006439982291319788,
    0.005725772142930000,
    0.005059403075507749,
    0.004441757628542499,
    0.003873099546309850,
    0.003353117075610484,
    0.002880973134926539,
    0.002455360952379100,
    0.002074563718984522,
    0.001736516788789891,
    0.001438870977808259,
    0.001179055567694071,
    0.000954339705406193,
    0.000761891003573287,
    0.000598830284134461,
    0.000462281565774996,
    0.000349416569001100,
    0.000257493196406908,
    0.000183887634646636,
    0.000126119913694109,
    0.000081872943140812,
    0.000049005219802397,
    0.000025557561404639,
    0.000009754363726571,
    0.000000000000000000,
    -0.000005128921027786,
    -0.000006894650075208,
    -0.000006411912043391,
    -0.000004663189391103,
    -0.000002514832169553,
    -0.000000733187507994,
    0.000000000000000000,
]
w3 = [
    -0.000000000000000003,
    0.009489865835136195,
    0.047599359273529158,
    0.121261259186275366,
    0.202402690898081855,
    0.238493649613954889,
    0.202402690898081855,
    0.121261259186275394,
    0.047599359273529186,
    0.009489865835136200,
    -0.000000000000000003,
]
w4 = [
    0.000000000000000000,
    0.000013345461113027,
    0.000074628325145084,
    0.000221840136667604,
    0.000503089050699102,
    0.000977933487489023,
    0.001716811061404203,
    0.002798105609275850,
    0.004302721212771339,
    0.006306412706846188,
    0.008870504732950237,
    0.012031960283269912,
    0.015793983968478750,
    0.020118426124570966,
    0.024921170591889922,
    0.030071442399851649,
    0.035395584801464423,
    0.040685371133555401,
    0.045710393533975331,
    0.050233572691654620,
    0.054028424473579854,
    0.056896454751228141,
    0.058682970302180941,
    0.059289706319876699,
    0.058682970302180948,
    0.056896454751228141,
    0.054028424473579854,
    0.050233572691654640,
    0.045710393533975338,
    0.040685371133555401,
    0.035395584801464423,
    0.030071442399851669,
    0.024921170591889922,
    0.020118426124570963,
    0.015793983968478739,
    0.012031960283269916,
    0.008870504732950243,
    0.006306412706846191,
    0.004302721212771345,
    0.002798105609275851,
    0.001716811061404202,
    0.000977933487489024,
    0.000503089050699102,
    0.000221840136667604,
    0.000074628325145085,
    0.000013345461113028,
    0.000000000000000000,
]

def filters(name, n_avg, A, B, w, fl, bl, typ):
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
    fig.tight_layout()
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
    fig2.tight_layout()
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
    ax1.set_title('IIR Sig' + name + ', A=' + str(A) + ', B=' + str(B))
    fig3.tight_layout()
    plt.savefig('plots/Sig' + name + '_iir.png')

    ### 7 FIR ###
    fir = []
    l = len(w)
    w = np.array(w)
    meas = np.array(meas)
    for i in range(len(meas)-l):
        fir.append(np.dot(w.T,meas[i:i+l])) #TODO
    t_fir = t[l:]

    fig4, ax1 = plt.subplots()
    ax1.plot(t,meas,'k')
    ax1.plot(t_fir, fir, 'r')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Amplitude')
    ax1.set_title('FIR Sig' + name + ', $n=$ ' + str(l) + ', $f_{L}=$ ' + str(fl) + '$Hz$, $b_{L}=$' + str(bl) + '$Hz$, ' + typ) #TODO: give further details (check Git syllabus)
    fig4.tight_layout()
    plt.savefig('plots/Sig' + name + '_fir.png')


name = 'A'
n_avg = 400 # mov avg
A = 0.9965 # IIR
B = 0.0035 # IIR
fl = 100
bl = 100
typ = 'Lowpass'
filters(name, n_avg, A, B, w1, fl, bl, typ)

name = 'B'
n_avg = 100 # mov avg
A = 0.985 # IIR
B = 0.015 # IIR
fl = 33
bl = 132
typ = 'Lowpass'
filters(name, n_avg, A, B, w2, fl, bl, typ)

name = 'C'
n_avg = 1 # mov avg
A = 0 # IIR
B = 1 # IIR
fl = 25
bl = 1225
typ = 'Lowpass'
filters(name, n_avg, A, B, w3, fl, bl, typ)

name = 'D'
n_avg = 45 # mov avg
A = 0.94 # IIR
B = 0.06 # IIR
fl = 8
bl = 40
typ = 'Lowpass'
filters(name, n_avg, A, B, w4, fl, bl, typ)



