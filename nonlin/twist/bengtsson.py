'''
second order chrmaticity
'''
from pylab import *

import matplotlib

font = {'size'   : 14}
matplotlib.rc('font', **font)

fig = plt.figure()
ax = fig.add_subplot(111)


nu  = np.linspace(0.01, 0.33, 100)

y = 6.*(cos(pi*nu) + cos(0.033*pi + pi*(1.-nu)))/sin(pi*nu) + 2.*(cos(3.*pi*nu) + cos(0.1*pi + 3.*pi*(1.-nu)))/sin(3.*pi*nu)

ax.plot(nu, y ,'r-', lw=3)
ax.set_ylabel(r'$\xi_x^{(2)}$')
ax.set_xlabel(r'$\nu_x$')

plt.show()
