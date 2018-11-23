# fodo lattice

from ocelot import *
from ocelot.gui.accelerator import *
from ocelot.cpbd.chromaticity import *
from pylab import *

from copy import deepcopy
from scipy.optimize import *

d1 = Drift (l = 0.2)
d2 = Drift (l = 0.2)
d3 = Drift (l = 0.2)
d4 = Drift (l = 0.2)
d5 = Drift (l = 0.1)
d6 = Drift (l = 0.1)
d7 = Drift (l = 0.4)



sf = Sextupole(l = 0.001, k2 = 5, id="sf")
sd = Sextupole(l = 0.001, k2 = -5, id="sd")

Q1 = Quadrupole (l = 0.293, k1 = 2.2)
Q2 = Quadrupole (l = 0.293, k1 = -2.2)

B1 = SBend(l = 2.0, angle = 0.04)
B2 = SBend(l = 1.227, angle = 0.04)

#fodo = (Q1, sf, D4, B1, D4, Q2, sd,  D4, B1, D4)
fodo = (Q1, d1, sf, d2, B1, d3, d4, Q2, d5, sd, d6, B1, d7) + (Q1, d1, sf, d2, B1, d3, d4, Q2, d5, sd,  d6, B1, d7)


m1 = Marker()
m2 = Marker()

cell = (m1,fodo*10,m2)

beam = Beam()
beam.E = 5.0
beam.beta_x = 0
beam.beta_y = 0
beam.alpha_x = 0
beam.alpha_y = 0


lat = MagneticLattice(cell)
tw0 = Twiss(beam)
tws=twiss(lat, Twiss())

c1, c2 = natural_chromaticity(lat, tws[0])
print 'natural chrom:', c1, c2
cx1, cx2 = sextupole_chromaticity(lat, tws[0])
print 'chrom/sext:', cx1, cx2

compensate_chromaticity(lat)

c1, c2 = natural_chromaticity(lat, tws[0])
print 'natural chrom:', c1, c2
cx1, cx2 = sextupole_chromaticity(lat, tws[0])
print 'chrom/sext:', cx1, cx2
print 'chrom:', chromaticity(lat, tws[0])

print sf.ms, sd.ms

plot_opt_func(lat, tws)
plt.show()
