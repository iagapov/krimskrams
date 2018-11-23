
from ocelot.gui.accelerator import *
import ocelot
from ocelot import *
from pylab import *
from ocelot.cpbd.chromaticity import *


from copy import deepcopy
from scipy.optimize import *

d0 = Drift (l = 4.5, eid = "D0")
qf = Quadrupole (l = 0.25, k1 = 1.5, eid = "QF")
qd = Quadrupole (l = 0.25, k1 = -1.5, eid = "QD")

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


tw0 = Twiss(beam)

ks = np.linspace(0,7,100)


k_a = []
mux_a = []
muy_a = []
dqx_a = []
dqy_a = []

for k in ks:
    qf.k1 = k
    qd.k1 = -k
    lat.update_transfer_maps()
    tws=twiss(lat, Twiss(), nPoints = 1000)
    if tws is None: print('no solution')
    else:
        dqx, dqy = natural_chromaticity(lat, tws[0])
        print(k, dqx, dqy, tws[-1].s, tws[-1].mux / (2.*pi), tws[-1].muy / (2.*pi))
        k_a.append(k)
        mux_a.append(tws[-1].mux / (2.*pi) / tws[-1].s)
        muy_a.append(tws[-1].muy / (2.*pi) / tws[-1].s)
        dqx_a.append(dqx / tws[-1].s)
        dqy_a.append(dqy / tws[-1].s)


plt.plot(k_a, mux_a)
plt.plot(k_a, dqx_a)
plt.grid(True)
plt.show()

#plot_opt_func(lat, tws, legend = False)
#plt.show()
