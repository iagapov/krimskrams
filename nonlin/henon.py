'''
Henon map
'''

from pylab import *



from numpy import sin
def henon(x0, y0, nt, a = 1.4, b=0.3):

    x = x0
    y = y0
    xs = [x0,]
    ys = [y0,]
    for i in range(nt):
        y = mod(y  + a * sin(x), 2*pi)
        x = mod(x + y, 2*pi)
        xs.append(x)
        ys.append(y)

    #return np.array(xs), mod(np.array(ys) + pi, 2*pi)
    return np.array(xs), mod(np.array(ys), 2*pi)

def plot_phase_space():

    for a in np.linspace(0.7, 2.12, 5):
        plt.figure()
        for x0 in np.linspace(0, 2*pi, 100):
            x, y = henon(x0,0.0, 1000)
            plt.plot(x,y,'.', color='black',alpha = 0.1)
    plt.show()

def plot_sm_freq():

    a = 0.9710 # 1.15
    fig, ax = plt.subplots()
    for x0 in np.linspace(0, 2*pi, 100):
        x, y = sm(x0,0.0, 1000, a=a)
        ax.plot(x,y,'.', color='black',alpha = 0.1)
    #plt.show()

    fig, ax = plt.subplots()
    fig2, ax2 = plt.subplots()
    fig3, ax3 = plt.subplots()

    for x0 in np.linspace(5.3, 5.3, 1):
        x, y = sm(x0,0.0, 1000, a=a)
        ax.plot(x,y,'.', color='black',alpha = 0.1)
        ax.grid(True)
        ax2.plot(x,'.--', color='black')
        ax2.grid(True)

        spx = np.fft.fft(x - np.mean(x))
        spx = np.abs(spx)
        spy = np.fft.fft(y - np.mean(y))
        spy = np.abs(spy)
        freq = np.fft.fftfreq(len(spx), d=1)

        ax3.plot(freq,spx,'.-', color='black')
        ax3.plot(freq,spy,'.--', color='black')


    for x0 in np.linspace(5.4, 5.4, 1):
        x, y = sm(x0,0.0, 1000, a=a)
        ax.plot(x,y,'.', color='blue',alpha = 0.1)
        ax.grid(True)
        ax2.plot(x,'.--', color='blue')
        ax2.grid(True)

        spx = np.fft.fft(x - np.mean(x) )
        spx = np.abs(spx)
        spy = np.fft.fft(y - np.mean(y))
        spy = np.abs(spy)
        freq = np.fft.fftfreq(len(spx), d=1)

        ax3.plot(freq,spx,'.-', color='blue')
        ax3.plot(freq,spy,'.--', color='blue')


    plt.show()

def scan_sm_freq():

    a = 2.2 # 1.15
    fig, ax = plt.subplots()

    qxs = []
    qx2s = []

    x0s = np.linspace(0, 2*pi, 100)

    for x0 in x0s:
        x, y = sm(x0,0.0, 1000, a=a)
        spx = np.fft.fft(x - np.mean(x))
        spx = np.abs(spx)
        freq = np.fft.fftfreq(len(spx), d=1)
        n = len(freq)/2
        qx = freq[0:n][argmax(spx[0:n])]
        ax.plot(x,mod(np.array(y)+pi, 2*pi),'.', color='black',alpha = 0.1)
        qxs.append(qx)

        x2, y2 = sm(x[-1],y[-1], 1000, a=a)
        spx = np.fft.fft(x2 - np.mean(x2))
        spx = np.abs(spx)
        qx2 = freq[0:n][argmax(spx[0:n])]
        qx2s.append(qx2)



    ax2 = ax.twinx()
    ax2.plot(x0s, qxs, '.', lw=3)

    # d2F/dx^2
    fig, ax3 = plt.subplots()
    ax3.plot(x0s[2:], np.diff(qxs,n=2), 'b.--', lw=3)
    ax4 = ax3.twinx()
    ax4.plot(x0s, np.array(qx2s) - np.array(qxs), 'r.--', lw=3)


    plt.show()


import scipy.integrate
import scipy.special

def pendulum_frequencies():

    a = 1.0

    hs = np.linspace(0.001, a, 100) # minus separatrix where frequency diverges
    ps = sqrt(2*(hs)) # cut at q=0
    vs = hs * 0

    for i in range(len(hs)):
        q0 = arccos(-hs[i] / a)
        qs = np.linspace(-q0, q0, 100)
        fs = 1. / sqrt(a + hs[i] + a * cos(qs))
        T = sqrt(2)*scipy.integrate.simps(fs,qs)
        vs[i] = 2 * pi / T

    plt.plot(ps,vs)

    plt.figure()
    ps = np.linspace(-1., 1., 100) # section qt q=pi, libration
    T = 1. / sqrt(ps**2 + 4*a) * scipy.special.ellipk( sqrt(4*a / (ps**2 + 4*a)) )
    vs = 2.*pi / T
    plt.plot(ps,vs)
    plt.show()


if __name__ == "__main__":
    plot_phase_space()
    #plot_sm_freq()
    #scan_sm_freq()
    #pendulum_frequencies()
