
from ocelot.gui.accelerator import *
import ocelot
from ocelot import *
from pylab import *
from ocelot.cpbd.chromaticity import *

from scipy.integrate import simps

from copy import deepcopy
from scipy.optimize import *

d0 = Drift (l = 5.0, eid = "D0")
qf = Quadrupole (l = 0.25, k1 = 0.9, eid = "QF")
qd = Quadrupole (l = 0.25, k1 = -0.9, eid = "QD")


b1=SBend(l=0.005, angle=0.001)
b2=SBend(l=0.005, angle=-0.001)
d0=(b1,b2,b2,b1)*200


fodo = (d0,qf, d0, qd)

beam = Beam()
beam.E = 6.0
beam.beta_x = 9.03267210229
beam.beta_y = 0.573294833302
beam.Dx = 2.0
beam.Dxp = 10.0
beam.beta_x = 0
beam.beta_y = 0
beam.Dx = 2.0
beam.Dxp = 10.0

lat = MagneticLattice( (fodo) )
tws=twiss(lat, Twiss(beam), nPoints=10000)

plot_opt_func(lat, tws, legend = False)

H = np.array([(1. + t.alpha_x**2)/ t.beta_x * t.Dx**2 + t.beta_x*t.Dxp**2 + 2*t.alpha_x*t.Dx*t.Dxp  for t in tws])
plt.figure()
plt.plot([t.s for t in tws], H)
print(simps(H,[t.s for t in tws]))


plt.show()
