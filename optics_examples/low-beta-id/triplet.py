
from ocelot.gui.accelerator import *
import ocelot
from ocelot import *
from pylab import *
from ocelot.cpbd.chromaticity import *


#ax1 = plt.figure().add_subplot(111)
#p1,=ax1.plot([0.3,0.5, 0.7, 1.0, 1.5, 2.0],[-4.7, -3.2, -2.5, -1.7, -1.2, -0.9], 'd--')
#p2,=ax1.plot([0.3,0.5, 0.7, 1.0, 1.5, 2.0],[-9.5, -6.8, -5.2, -3.7, -2.8, -2.2], 'd--')
#ax1.set_xlabel(r'$\beta^{*}$, m')
#ax1.legend([p1,p2],[r'$\xi_{X}$',r'$\xi_{Y}$'])
#plt.show()
#exit(0)


from copy import deepcopy
from scipy.optimize import *

d0 = Drift (l = 5.0, eid = "D0")
d1 = Drift (l = 1.5, eid = "D1")
d2 = Drift (l = 1.3, eid = "D2")
d3 = Drift (l = 5.0, eid = "D3")

q1 = Quadrupole (l = 0.25, k1 = 1.4, eid = "Q1")
q2 = Quadrupole (l = 0.25, k1 = -2.15, eid = "Q2")
q3 = Quadrupole (l = 0.25, k1 = 1.4, eid = "Q3")



insh  =  (d0,q1, d1, q2, d2, q3, d3)
ip = Marker()
mend = Marker()
ins = (insh[::-1], ip, insh, mend)


beam = Beam()
beam.E = 6.0
beam.beta_x = 6.6
beam.beta_y = 2.1
beam.alpha_x = 0.0
beam.alpha_y = 0.0
lat = MagneticLattice( ins )


tw0 = Twiss(beam)

tws=twiss(lat, tw0, nPoints = 1000)
#tws=twiss(lat, Twiss(), nPoints = 1000)
dqx, dqy = natural_chromaticity(lat, tws[0])
print(dqx, dqy)
plot_opt_func(lat, tws, legend = False)
plt.show()


constr = {}
constr['global'] = {'beta_x':['<',100], 'beta_y':['<',35]}
constr[ip] = {'beta_x':1.0, 'alpha_y':0.0, 'beta_y':6.0, 'alpha_y':0.0 }
constr[mend] = {'beta_x':6.6, 'alpha_y':0.0, 'beta_y':2.1, 'alpha_y':0.0 }

varz = [q1,q2,q3, d1, d2, d3]
match(lat, constr, varz, tw0, max_iter=50000, method='simplex')

print('values:')
for v in varz:
    if v.__class__ in (Quadrupole, SBend):
        print(v.id, '=', v.k1)
    if v.__class__ in (Drift,):
        print(v.id, 'l=', v.l)

lat.update_transfer_maps()

tws=twiss(lat, tw0, nPoints = 1000)
#tws=twiss(lat, Twiss(), nPoints = 1000)
dqx, dqy = natural_chromaticity(lat, tws[0])
print(dqx, dqy)
plot_opt_func(lat, tws, legend = False, top_plot=['mux', 'muy'])
plt.show()


__tws__ = tw0
__lattice_list__ = {'id': (ins, __tws__)}
__lattice__, __tws__ = __lattice_list__['id']
__knobs__ = None
