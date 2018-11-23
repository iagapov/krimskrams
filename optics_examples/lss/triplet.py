
from ocelot.gui.accelerator import *
import ocelot
from ocelot import *
from pylab import *
from ocelot.cpbd.chromaticity import *


from copy import deepcopy
from scipy.optimize import *

d0 = Drift (l = 6.0, eid = "D0")
d1 = Drift (l = 0.5, eid = "D1")
d2 = Drift (l = 0.5, eid = "D2")

q1 = Quadrupole (l = 0.25, k1 = 1.1, eid = "Q1")
q2 = Quadrupole (l = 0.25, k1 = -2.2, eid = "Q2")
q3 = Quadrupole (l = 0.25, k1 = 1.1, eid = "Q3")



tpl =  (d0,q1, d1, q2, d2, q3, d0)


beam = Beam()
beam.E = 6.0
lat = MagneticLattice( (tpl,tpl,tpl,tpl) )


tw0 = Twiss(beam)

ks = np.linspace(0.1,5,50)

k_a = []
mux_a = []
muy_a = []
dqx_a = []
dqy_a = []

for k in ks:
    q2.k1 = -k
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



plt.plot(k_a, mux_a, 'b-')
plt.plot(k_a, muy_a, 'g-')
plt.plot(k_a, dqx_a, 'b--')
plt.plot(k_a, dqy_a, 'g--')
plt.grid(True)
plt.show()

q2.k1 = -2.2
lat.update_transfer_maps()

tws=twiss(lat, Twiss(beam), nPoints=1000)
plot_opt_func(lat, tws, legend = False)
plt.show()
