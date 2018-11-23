# need to rememberr

from ocelot.gui.accelerator import *
import ocelot
from ocelot import *
from pylab import *



from copy import deepcopy
from scipy.optimize import *

d0 = Drift (l = 0.7, eid = "D0")
qf = Quadrupole (l = 0.1, k1 = 8.45, eid = "QF")
b1 = SBend(l = 1.0, angle = 0.006 , k1 = -2.04, eid  = "B1")

m1 = Marker(eid="start")
m2 = Marker(eid="end")

tme = (qf, d0, b1, d0, qf)

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


lat = MagneticLattice( (40*tme) )
tw0 = Twiss(beam)
#tws=twiss(lat, tw0, nPoints = 1000)
tws=twiss(lat, Twiss(), nPoints = 1000)
plot_opt_func(lat, tws, legend = False)


eb = EbeamParams(lat, beam, nsuperperiod=1)
print(eb)
#print("Je:", eb.I4)

#print(eb.integrals_id())
#print (eb.I5, eb.I2,eb.I4)
#print ( (6000.0 / 0.511)**2 * 0.383 * eb.I5 / (eb.I2 - eb.I4) )


plt.show()
