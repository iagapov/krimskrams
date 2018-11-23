'''
map plots
'''
from pylab import *


global mux, muy

mux = 0.01 + 1./2. * pi *2.
muy = 0.01 + 1./2. * pi * 2.

# sextupole with a twist
def half_map_sext_t(x,xp, y, yp, ms=0.1):
    x2 = cos(mux) * y + sin(mux) * yp
    y2 = -1* ( -cos(muy) * x - sin(muy) * xp )
    xp2 = -sin(mux) * y + cos(mux) * yp
    yp2 = -1 * (sin(muy) * x - cos(muy) * xp )

    xp2 = xp2 - ms*(x2**2 - y2**2)
    yp2 = yp2 + 2*ms * x2*y2

    return x2, xp2, y2, yp2

# sextupole w/o twist
def half_map_sext(x,xp, y, yp, ms=0.1):
    x2 = cos(mux) * x + sin(mux) * xp
    y2 = cos(muy) * y + sin(muy) * yp
    xp2 = -sin(mux) * x + cos(mux) * xp
    yp2 = -sin(muy) * y + cos(muy) * yp

    xp2 = xp2 - ms*(x2**2 - y2**2)
    yp2 = yp2 + 2*ms * x2*y2

    return x2, xp2, y2, yp2

# octupole w/o twist
def half_map_oct(x,xp, y, yp, mo=0.1):
    x2 = cos(mux) * x + sin(mux) * xp
    y2 = cos(muy) * y + sin(muy) * yp
    xp2 = -sin(mux) * x + cos(mux) * xp
    yp2 = -sin(muy) * y + cos(muy) * yp

    xp2 = xp2 + mo*(x2**3 / 3. - x2*y2**2)
    yp2 = yp2 + mo*(y2**3 / 3. - x2**2 * y2)

    return x2, xp2, y2, yp2

# octupole with twist
def half_map_oct_t(x,xp, y, yp, mo=0.1):

    x2 = cos(mux) * y + sin(mux) * yp
    y2 = -1 * (-cos(muy) * x - sin(muy) * xp)
    xp2 = -sin(mux) * y + cos(mux) * yp
    yp2 = -1 * (sin(muy) * x - cos(muy) * xp )

    xp2 = xp2 + mo*(x2**3 / 3. - x2*y2**2)
    yp2 = yp2 + mo*(y2**3 / 3. - x2**2 * y2)

    return x2, xp2, y2, yp2


def plot_phase_space(x0, xp0, ax1, ax2):
    ar_x = []
    ar_xp = []
    ar_y = []
    ar_yp = []

    y0 = 0.0
    yp0 = 0.0

    x = x0
    y=y0
    xp=xp0
    yp=yp0
    for i in range(10000):
        x, xp, y, yp = half_map_sext(x,xp,y,yp, 0.5)
        x, xp, y, yp = half_map_sext(x,xp,y,yp, 0.5)

        if abs(x) > 100 or abs(xp) > 100 or abs(y) > 100 or abs(yp) > 100 :
            break
        ar_x.append(x)
        ar_xp.append(xp)
        ar_y.append(y)
        ar_yp.append(yp)

    ax1.plot(ar_x, ar_xp, 'C0.', alpha=0.3)
    ax1.set_xlabel(r'$X$')
    ax1.set_ylabel(r'$X\prime$')
    ax2.plot(ar_y, ar_yp, 'C0.', alpha=0.3)
    ax2.set_xlabel(r'$Y$')
    ax2.set_ylabel(r'$Y\prime$')


ax1 = plt.figure().add_subplot(111)
ax2 = plt.figure().add_subplot(111)

for x0 in np.linspace(-18.1, -13.00, 100):
    for xp0 in np.linspace(-80.0, -80.0, 1):
        plot_phase_space(x0, xp0, ax1, ax2)

plt.show()
sys.exit(0)


def plot_freq_diagram():
    global mux, muy
    da = []
    for mx in np.linspace(0.001, pi, 50):
        for my in np.linspace(0.001, pi, 50):
            mux = mx
            muy = my
            x = 0.3
            y = 0.2
            xp=0.
            yp=0.
            lost = False
            print('checking {} {}'.format(mux, muy) )
            for i in range(10000):
                x, xp, y, yp = half_map_sext_t(x,xp,y,yp, 0.5)
                x, xp, y, yp = half_map_sext_t(x,xp,y,yp, 0.5)
                if abs(x) > 100 or abs(xp) > 100 or abs(y) > 100 or abs(yp) > 100 :
                    lost = True
                    print( '{} {} lost'.format(mux,muy))
                    break
            if not lost:
                print( '{} {} not slost'.format(mux,muy))
                da.append( (2*mx/(2.*pi), 2*my/(2.*pi) ) )


    print('da {}'.format(da))

    ax1 = plt.figure().add_subplot(111)
    ax1.plot([z[0] for z in da], [z[1] for z in da], '.')
    ax1.set_xlabel(r'$2 \mu_x$')
    ax1.set_ylabel(r'$2 \mu_y$')
    plt.show()


#plot_freq_diagram()
#plt.show()
#sys.exit(0)


da = []
for x0 in np.linspace(-1.0, 1.0, 100):
    for y0 in np.linspace(-1.0, 1.0, 100):
        x=x0
        y=y0
        xp=0.0
        yp=0.0

        lost = False

        for i in range(10000):
            x, xp, y, yp = half_map_sext(x,xp,y,yp, 0.5)
            x, xp, y, yp = half_map_sext(x,xp,y,yp, 0.5)

            if abs(x) > 100 or abs(xp) > 100 or abs(y) > 100 or abs(yp) > 100 :
                lost = True
                print('{} lost'.format(x0) )
                break

        if not lost:
            da.append((x0,y0))


ax = plt.figure().add_subplot(111)
ax.plot([z[0] for z in da], [z[1] for z in da], 'C0.')
ax.set_xlabel(r'$X$')
ax.set_ylabel(r'$Y$')

plt.show()
