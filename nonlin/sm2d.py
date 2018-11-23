'''
frequency analysis:
standad map
'''

from pylab import *


''' test mapping '''

from numpy import sin
def sm2d(x10, y10, x20, y20, nt, a1 = 2.6, a2=2.6, b=0.1):

    x1 = x10
    x2 = x20
    y1 = y10
    y2 = y20


    x1s = [x10,]
    y1s = [y10,]
    x2s = [x20,]
    y2s = [y20,]

    for i in range(nt):
        x1p = mod(x1 + a1*sin(x1+y1) + b* sin(0.5*(x1+y1+x2+y2)),   2*pi)
        y1p = mod(x1 + y1, 2*pi)
        x2p = mod(x2 + a2*sin(x2+y2) + b* sin(0.5*(x1+y1+x2+y2)),   2*pi)
        y2p = mod(x2 + y2, 2*pi)

        x1 = x1p
        x2 = x2p
        y1 = y1p
        y2 = y2p

        x1s.append(x1)
        y1s.append(y1)
        x2s.append(x2)
        y2s.append(y2)


    return np.array(x1s),np.array(y1s),np.array(x2s),np.array(y2s)


def frequencies(x1,y1,x2,y2):

    spy1 = np.fft.fft(y1 - np.mean(y1))
    spy1 = np.abs(spy1)
    spy2 = np.fft.fft(y2 - np.mean(y2))
    spy2 = np.abs(spy2)
    freq = np.fft.fftfreq(len(spy1), d=1)
    n = int(len(freq)/2)
    q1 = freq[0:n][argmax(spy1[0:n])]
    q2 = freq[0:n][argmax(spy2[0:n])]

    return q1, q2

def plot_phase_space():

    for b in np.linspace(0.0, 0.01, 5):
        fig, ax = plt.subplots()
        q1s = []
        q2s = []
        for y0 in np.linspace(0, 2*pi, 200):
            x1, y1, x2, y2 = sm2d(0.0,-sqrt(0.4), 0.0, y0, nt=2000, a1=1.3, a2=1.3, b=b)
            ax.plot(y2, mod(x2+pi, 2*pi),'.', color='black',alpha = 0.1)

            q1, q2 = frequencies(x1, y1, x2, y2)

            q1s.append(q1)
            q2s.append(q2)

        ax2 = ax.twinx()
        #fig2, ax2 = plt.subplots()
        ax2.plot(np.linspace(0, 2*pi, 200), q1s,'.--', color='blue')
        ax2.plot(np.linspace(0, 2*pi, 200), q2s,'.--', color='red')


    plt.show()


def freq_diagram():
    b = 0.01
    fig, ax = plt.subplots()
    fig2, ax2 = plt.subplots()

    y10s = np.linspace(0.1, 0.1, 1)
    y20s = np.linspace(0.09, 0.09, 1)



    q1s = []
    q2s = []
    for i in range(len(y10s)):
        for j in range(len(y20s)):

            x10, y10, x20, y20 = 0.0, y10s[i], 0.0, y20s[j]
            for nt in range(0,200):

                x1, y1, x2, y2 = sm2d(x10,y10, x20, y20, nt=1000, a1=1.3, a2=1.3, b=b)
                x10, y10, x20, y20 = x1[-1], y1[-1], x2[-1], y2[-1]

                q1, q2 = frequencies(x1, y1, x2, y2)

                ax.plot(y1, y2,'.', color='black',alpha = 0.1)
                q1s.append(q1)
                q2s.append(q2)

    ax2.plot(q1s[0], q2s[0],'rd')
    ax2.plot(q1s, q2s,'.', color='blue', alpha=0.4)
    plt.show()



if __name__ == "__main__":
    #plot_phase_space()
    freq_diagram()
