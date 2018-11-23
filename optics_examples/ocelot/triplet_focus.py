'''
focusing triplet, collider-like
'''


from ocelot import *
from ocelot.gui.accelerator import *
from ocelot.cpbd.chromaticity import *



qrf1 = Quadrupole(l=0.2, k1 = 2)
qrf2 = Quadrupole(l=0.2, k1 = -4)
qrf3 = Quadrupole(l=0.2, k1 = 4.1)

qrf1.k1 = 1.83880828901
qrf2.k1 = -4.24668111472
qrf3.k1 = 4.25273945407


qrf4 = Quadrupole(l=0.2, k1 = 3.9)
qrf5 = Quadrupole(l=0.2, k1 = -5.0)
qrf6 = Quadrupole(l=0.2, k1 = 2.5)


drf1 = Drift(l=1)
drf2 = Drift(l=0.5)
drf3 = Drift(l=0.5)
drf4 = Drift(l=7.9)
drf5 = Drift(l=0.5)
drf6 = Drift(l=0.5)
drf7 = Drift(l=1)

mrfs = Marker()
mrfe = Marker()

rf_cell = (mrfs, drf1, qrf1, drf2, qrf2, drf3, qrf3, drf4, qrf3, drf5, qrf2, drf6, qrf1, drf7, mrfe )

beam = Beam()
beam.E = 5.0
beam.beta_x = 10
beam.beta_y = 5
beam.alpha_x = 3.
beam.alpha_y = 3.


# variable names for lattice designer
__lattice__ = rf_cell
__beam__ = beam
__tws__ = Twiss(beam)



