
from ocelot.gui.accelerator import *
import ocelot
from ocelot import *
from pylab import *
from ocelot.cpbd.chromaticity import *


from copy import deepcopy
from scipy.optimize import *

d0 = Drift (l = 7.0, eid = "D0")
d1 = Drift (l = 0.5, eid = "D1")
d2 = Drift (l = 0.5, eid = "D2")

q1 = Quadrupole (l = 0.25, k1 = 1.2, eid = "Q1")
q2 = Quadrupole (l = 0.25/2., k1 = -2.2, eid = "Q2")
q3 = Quadrupole (l = 0.25, k1 = 1.1, eid = "Q3")


d0m = Drift (l = 4.2, eid = "D0")
d1m = Drift (l = 0.5, eid = "D1")
d2m = Drift (l = 0.5, eid = "D2")

q1m = Quadrupole (l = 0.25, k1 = 1.6, eid = "Q1")
q2m = Quadrupole (l = 0.25, k1 = -2.9, eid = "Q2")
q3m = Quadrupole (l = 0.25, k1 = 1.6, eid = "Q3")

fp3 = Marker()
tpl =  (d0,q1, d1, q2, q2, d2, q3, d0)
tplm = (d0m,q1m, d1m, q2m, d2m, q3m, d0m)

beam = Beam()
beam.E = 6.0
beam.beta_x = 5.0
beam.beta_y = 2.0

lat = MagneticLattice( tpl )
tws=twiss(lat, Twiss())

fp1 = Marker()
fp2 = Marker()
lat2 = MagneticLattice( (tplm, fp1, tpl, (d0,q1, d1, q2, fp3, q2, d2, q3, d0), tpl, tplm[::-1], fp2) )

constr = {fp2:{'beta_x':beam.beta_x, 'beta_y':beam.beta_y,'alpha_x':0.0,
    'alpha_y':0.0,'mux':2.*pi, 'muy':2.*pi}}
constr[fp1] = {'alpha_x':0.0, 'alpha_y':0.0}
constr[fp3] = {'alpha_x':0.0, 'alpha_y':0.0}
vars = [q1m,q2m,q3m, q1, q2, q3]
match(lat2, constr, vars, Twiss(beam), max_iter=10000)

print(q1m.k1, q2m.k1, q3m.k1, q1.k1, q2.k1, q3.k1)


tws=twiss(lat2, Twiss(beam), nPoints=1000)

#print tws[-1].mux /(2.*pi)
#print tws[-1].muy /(2.*pi)
#print tws[-1].alpha_x
#print tws[-1].alpha_y
#print tws[-1].beta_x
#print tws[-1].beta_y
dqx, dqy = natural_chromaticity(lat2, tws[0])
#print('chrom:',dqx, dqy)


plot_opt_func(lat2, tws, legend = False)
plt.show()
