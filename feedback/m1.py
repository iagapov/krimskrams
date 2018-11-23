from pylab import *
from scipy.optimize import *
from scipy import optimize


l = 2.9
dt = 0.01


v = 0.07
x = 0.0
t = 0.0

xa = []
va = []

v0 = 0.1

def fb_gain(v):
    #return 20.0*(v0 - v)
    if abs(v-v0)>0.001: return 0.05 * sign(v0-v)
    return 0.9*(v0 - v)

vhist = 0

while t < 10.0:
    t = t + dt
    x = x + dt*v
    v = v + dt*fb_gain(vhist) + dt*0.01*np.random.randn()
    xa.append(x)
    va.append(v)
    if t > dt*15: vhist = va[-11]

ax = plt.figure().add_subplot(111)
ax.plot(va,'.--')

plt.show()
