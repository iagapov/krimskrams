# controlling non-linear oscillator

from pylab import *
from scipy.optimize import *
from scipy import optimize


l = 2.9
dt = 0.01
T = 100.0
alpha = 0.1

v = 0.07
x = 0.0
t = 0.0

xa = []
va = []

v0 = 0.0

def fb_gain(v):
    #return 20.0*(v0 - v)
    #if abs(v-v0)>0.001: return 0.05 * sign(v0-v)
    return 0.9*(v0 - v)

vhist = 0

while t < T:
    t = t + dt
    x = x + dt*v
    v = v - dt*x - alpha * x**2 + dt*0.1*np.random.randn() + dt*fb_gain(vhist)
    xa.append(x)
    va.append(v)
    if t > dt*15: vhist = va[-11]

ax = plt.figure().add_subplot(111)
ax.plot(va,'.--')
#ax.plot(xa,va,'.')

plt.show()
