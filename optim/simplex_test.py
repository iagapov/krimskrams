from pylab import *
from scipy.optimize import *
from scipy import optimize

a0 = 0.1
sig = 0.01
w0 = 100.11

def f(x,t):
    x0 = 1.0 + a0* sin(w0 * t)
    a = 1. + np.random.randn() * sig
    return  a*exp(-(x-x0)**2/2)


x = np.linspace(-5,5)

for t in np.linspace(0, 10, 100):
    plt.plot(x,f(x, t), 'b-', alpha = 0.1)


def err_f(x):
    global tau
    tau += 1.0
    trace_x.append(x)
    trace_f.append(f(x, tau))
    trace_t.append(tau)
    #print tau, x
    return -f(x, tau)

ax = plt.figure().add_subplot(111)
ax2 = plt.figure().add_subplot(111)
#ax2 = ax.twinx()

for i in np.linspace(1,10, 100):

    x = [0.0]
    tau = 0.0 + 100*np.random.randn()
    trace_x = []
    trace_f = []
    trace_t = []


    isim = array([[-5.e-2,  5.e-2]]).T
    optimize.minimize(err_f, x, method="Nelder-Mead", options={'disp': False, 'initial_simplex': isim, 'maxiter': 100, 'xatol':1.e-5 })

    print(trace_x[-1])

    trace_x = np.array(trace_x)
    trace_f = np.array(trace_f)
    trace_t = np.array(trace_t)

    ax.plot(trace_t - trace_t[0], trace_x, 'r-', alpha=0.8)
    ax2.plot(trace_t - trace_t[0], trace_f, 'g-', alpha=0.1)



plt.show()
