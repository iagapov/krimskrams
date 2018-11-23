'''
fodo
'''


from ocelot import *
from ocelot.gui.accelerator import *
from ocelot.cpbd.chromaticity import *



qf = Quadrupole(l=0.2, k1 = 2)
qd = Quadrupole(l=0.2, k1 = -2)
d1 = Drift(l=1.)

f_cell = (qf,d1,qd,d1,qf,d1,qd,d1 )

beam = Beam()
beam.E = 5.0
beam.beta_x = 10
beam.beta_y = 5
beam.alpha_x = 3.
beam.alpha_y = 3.


# variable names for lattice designer
__lattice__ = f_cell
__beam__ = beam
__tws__ = Twiss(beam)



