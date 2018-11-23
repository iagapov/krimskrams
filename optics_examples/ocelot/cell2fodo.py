'''
cell 2 fodo
'''


from ocelot import *
from ocelot.gui.accelerator import *
from ocelot.cpbd.chromaticity import *


qm1 = Quadrupole(l=0.2, k1 = -1)
qm2 = Quadrupole(l=0.2, k1 = 1.9)
d1 = Drift(l=0.01)
d2 = Drift(l=1.)
d3 = Drift(l=0.8)

qf = Quadrupole(l=0.2, k1 = 0.9)
qd = Quadrupole(l=0.2, k1 = -0.9)
df = Drift(l=7.7)

f_cell = (d1,qm1,d2,qm2,d3,qf,df,qd,df,qf,df,qd,df, qf,df,qd,df,qf,df,qd,df, qf, d3, qm2, d2, qm1, d1 )

beam = Beam()
beam.E = 5.0
beam.beta_x  = 2.83565998873
beam.beta_y  = 26.6776307783
beam.alpha_x = -2.63151863804
beam.alpha_y = 2.88797252516

# variable names for lattice designer
__lattice__ = f_cell
__beam__ = beam
__tws__ = Twiss(beam)



