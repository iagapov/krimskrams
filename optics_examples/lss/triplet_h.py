
from ocelot.gui.accelerator import *
import ocelot
from ocelot import *
from pylab import *
from ocelot.cpbd.chromaticity import *
from scipy.integrate import simps


from copy import deepcopy
from scipy.optimize import *

d0 = Drift (l = 2.0, eid = "D0")
d1 = Drift (l = 0.5, eid = "D1")
d2 = Drift (l = 0.5, eid = "D2")

q1 = Quadrupole (l = 0.25, k1 = 2.7, eid = "Q1")
q2 = Quadrupole (l = 0.25, k1 = -4.2, eid = "Q2")
q3 = Quadrupole (l = 0.25, k1 = 2.6, eid = "Q3")



b1=SBend(l=0.005, angle=0.001)
b2=SBend(l=0.005, angle=-0.001)
d0=(b1,b2,b2,b1)*100

tpl =  (d0,q1, d1, q2, d2, q3, d0)


beam = Beam()
beam.E = 6.0
lat = MagneticLattice( (tpl,tpl) )


tw0 = Twiss(beam)
lat.update_transfer_maps()

tws=twiss(lat, Twiss(beam), nPoints=10000)
plot_opt_func(lat, tws, legend = False)


H = np.array([(1. + t.alpha_x**2)/ t.beta_x * t.Dx**2 + t.beta_x*t.Dxp**2 + 2*t.alpha_x*t.Dx*t.Dxp  for t in tws])
plt.figure()
plt.plot([t.s for t in tws], H)
print(simps(H,[t.s for t in tws]))



plt.show()
