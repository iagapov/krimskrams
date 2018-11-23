# fodo lattice

from ocelot import *
from ocelot.gui.accelerator import *
from ocelot.cpbd.chromaticity import *
from pylab import *

from copy import deepcopy
from scipy.optimize import *

D4 = Drift (l = 0.33)

SF = Sextupole(l = 0, ms = 100.7673786254063251)
SD = Sextupole(l = 0, ms = -300.6169817233025707)

Q1 = Quadrupole (l = 0.293, k1 = 1.39)
Q2 = Quadrupole (l = 0.293, k1 = -1.39)


B1 = SBend(l = 2.0, angle = 0.04)
B2 = SBend(l = 1.227, angle = 0.04)

fodo = (Q1,D4, B1, D4, Q2, D4, B1, D4)


m1 = Marker()
m2 = Marker()

cell = (m1,fodo,m2)

beam = Beam()
beam.E = 5.0
beam.beta_x = 0
beam.beta_y = 0
beam.alpha_x = 0
beam.alpha_y = 0



lat = MagneticLattice(cell)
tw0 = Twiss(beam)
tws=twiss(lat, Twiss())
plot_opt_func(lat, tws)

mux = []
muy = []
I2 = []
I5 = []
cx = []
cy = []


for k in linspace(0.7, 2.39, 20):
    Q1.k1 = k
    Q2.k1 = -k
    lat.update_transfer_maps()
    tws=twiss(lat, Twiss(), nPoints = 1000)
    c1, c2 = natural_chromaticity(lat, tws[0])
    mux.append(tws[-1].mux * 180 / pi )
    muy.append(tws[-1].muy * 180 / pi)
    eb = EbeamParams(lat, beam, nsuperperiod=1)
    I2.append(eb.I2)
    I5.append(eb.I5)
    cx.append(c1)
    cy.append(c2)



fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(mux, np.array(I5) * 1.e6, lw = 3)
ax.set_xlabel(r'$\mu_x$')
ax.set_ylabel(r'$I_5, 10^{-6}$')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(mux, cx, lw = 3)
ax.plot(mux, cy, lw = 3)
ax.set_xlabel(r'$\mu_x$')
ax.set_ylabel(r'$\xi_x, \xi_y$')



plt.show()
