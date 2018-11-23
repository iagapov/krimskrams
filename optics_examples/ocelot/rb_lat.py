'''
Moebius-based P4
curent
'''


from ocelot import *
from ocelot.gui.accelerator import *
from ocelot.cpbd.chromaticity import *


b_ang = 0.000981747704248221 * 0.89

bk1 = -1.297
bk2 = -1.297


m1 =  Marker()

m2 =  Marker()

m3 = Marker()

d1 = Drift(l=0.2)
d2 = Drift(l=1.0)
d3 = Drift(l=1.1)
d4 = Drift(l=0.05)

d3e = Drift(l=2.46)

qd1 = Quadrupole(l=0.23, k1=-1.773388770616)

qd2 = Quadrupole(l=0.2, k1=-1.74)
#qd2 = Quadrupole(l=0.2, k1=-2.2184407165)

#qf1 = Quadrupole(l=0.2, k1=2.75452)
qf1 = SBend(l=0.2, angle=0.0009,  k1=2.75452)

#qf2 = Quadrupole(l=0.2, k1=3.37)
qf2 = Quadrupole(l=0.2, k1=3.62733647558)

qf2e = Quadrupole(l=0.2, k1=3.62733647558)

b0 = SBend(l=0.1, angle=b_ang, k1=bk1)
b1 = SBend(l=0.1, angle=b_ang, k1=bk2)


b2 = SBend(l=0.1, angle=b_ang, k1=0.00)
b2e = SBend(l=0.1, angle=b_ang*1.05, k1=0.00)

sf1 = Sextupole(l=0.25, k2= 195.0, id='sf1')  # dqx + dqy = +0
#nsext = 5 # splitting sextupole for tracking
#sf1 = ( (Sextupole(l=sf1.l / nsext , k2= 195.  ), ) * nsext)


#rfc =  Cavity(l=0.0001, volt=100. / 0.0001, phi = pi/2., freq=500.0e6)

rfc = Marker()


be0 =(b0,b0,b0,b0,b0,b0,b0,b0)

be1 =(b1,b1,b1,b1,b1,b1,b1,b1)

block1 = (qf1,d1,be0,d1,qf1)

block2 = (qf1,d1,be0,d1,qf1)
block3 = (qf1,d1,be1,d2,m1,sf1,d4,qf2,d3,b2,b2,b2,b2,b2,b2,b2,b2,b2,d1,qd2)
celarc = (block3[::-1],block1,block1,block3)

block3e = (qf1,d1,be1,d2,m1,sf1,d4,qf2e,d3e,b2e,b2e,b2e,b2e,b2e,b2e,b2e,b2e,b2e,d1, qd2)
celarce = (block3[::-1],block1,block1,block3e)
celarcs = (block3e[::-1],block1,block1,block3)


block3_short = (d4,qf2,d3,b2,b2,b2,b2,b2,b2,b2,b2,b2,d1,qd2) # between sextupoles
celarc_short = (block3_short[::-1],block1,block1,block3_short)

iid_transform = Matrix(rm13=-1., rm24=-1.0, rm31=1.0, rm42=1.0, l = 0.0 )
id_transform = Matrix(rm11=1., rm22=1.0, rm33=1.0, rm44=1.0, l=0.0 )

#betay = 15.165327182
#betax = 0.48939051862

betax  = 0.806760276534
betay  = 12.5996504284


iidm = Matrix(rm13=-sqrt(betax/betay), rm24=-sqrt(betay/betax), rm31=sqrt(betay/betax), rm42=sqrt(betax/betay), l = 0.0000 )

exss = (iidm)

ss = Marker()


# rf 

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

rfc = Cavity(l=7.9, volt = 20.e6, freq = 498.89e6, phi = 90 )
#rfc = Drift(l=7.9)

mrfs = Marker()
mrfe = Marker()

rf_cell = (mrfs, drf1, qrf1, drf2, qrf2, drf3, qrf3, rfc, qrf3, drf5, qrf2, drf6, qrf1, drf7, mrfe )
#rf_cell = (mrfs, drf1, qrf1, drf2, qrf2, drf3, qrf3, drf4, qrf4, drf5, qrf5, drf6, qrf6, drf7, mrfe )

celarc1 = (celarc*16, celarce, rf_cell, celarcs, celarc*16) 
machine = (celarc1, exss, celarc*32, ss,  celarc*32, exss, celarc*32,ss)

beam = Beam()
beam.E = 5.0

# variable names for lattice designer
__lattice__ = celarc
__beam__ = beam
__tws__ = None