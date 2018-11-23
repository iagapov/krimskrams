'''
cell for arcs with insertions
'''

from ocelot import *
from ocelot.gui.accelerator import *
from ocelot.cpbd.chromaticity import *

np.set_printoptions(precision=6, suppress=True, linewidth=120)

ang_scale = 1.0


bk1 = -1.3755
bk2 = -1.3755

m1 = Marker()
m2 = Marker()
m3 = Marker()
mcellee = Marker()


d10 = Drift(l=0.18835)
d1 = Drift(l=0.18835)
d2 = Drift(l=1.045)
d3 = Drift(l=0.7534)
d4 = Drift(l=0.0471)

d3e = Drift(1.26870121472)

qd1 = Quadrupole(l=0.0471, k1=-8.2983, eid="qd1")
qd2 = Quadrupole(l=0.18835, k1=-2.007, eid="qd2")
qd2e = Quadrupole(l=0.18835, k1=-6.8, eid="qd2e")
qd3 = Quadrupole(l=0.2, k1=-0.1, eid="qd3")

qf1 = Quadrupole(l=0.18835, k1=2.5594, eid="qf1")
qf2a = Quadrupole(l=0.09418, k1=3.890, eid="qf2a")
qf2b = Quadrupole(l=0.09418, k1=3.890, eid="qf2b")

qmd2e = Quadrupole(l=0.2, k1=-1.74472371472)

qf0 = Quadrupole(l=0.18835, k1=3.0104, eid="qf0")
b0 = SBend(l=0.09418, angle=0.000972*ang_scale, k1=bk1)
b1 = SBend(l=0.09418, angle=0.000972*ang_scale, k1=0)


b2 =  SBend(l=0.09418, angle=0.0010*ang_scale, k1=0)
b2e = SBend(l=0.1, angle=0.0010*ang_scale, k1=0.00)


sf1 = Sextupole(l=0.2825, k2= 243.5, eid="sf1")
nsext = 5 # splitting sextupole for tracking
sf1 = ( (Sextupole(l=sf1.l / nsext , k2= 243.5  ), ) * nsext)


ud1 = Drift(l=0.1)
ud1e = Drift(l=0.2)
ud2 = Drift(l=0.1)
ud2e = Drift(l=0.1)
uq0 = Quadrupole(l=0.2, k1=0.1, eid="uq0")
uq0e = Quadrupole(l=0.2, k1=0.1, eid="uq0e")
uq1 = Quadrupole(l=0.2, k1=-0.1, eid="uq1")
ud0 = Drift(l=0.1)
ud0e = Drift(l=3.21)


be0 =(b0,b0,b0,b0,b0,b0,b0,b0)
be1 = (b1,b1,b1,b1,qd1,qd1,b1,b1,b1,b1)

b1m = SBend(l=0.09418, angle=0.000972*ang_scale, k1=qd1.k1 * qd1.l / (qd1.l + 4. * b1.l))


qd2.k1 = -7.1
qf2a.k1 = 6.7
qf2b.k1 = 3.69
uq0.k1 = 7.1
uq0e.k1 = 7.1
uq1.k1 = -0.0
b1m.k1 = -0.81
qd3.k1=  -0.8
b0.k1 = -1.25
b1.k1 = 0
qf1.k1 = 2.6
qf0.k1 = 3.0

ud0.l = 3.21
ud1.l = 0.2
ud2.l = 0.5
ud2e.l = 0.5
uq0.l=0.2
uq0e.l=0.2
uq1.l=0.2
d1.l = 0.1
d3.l = 0.63
d2.l = 0.32

b0.angle = 0.0009*ang_scale
b1.angle = 0.0014*ang_scale
b2.angle = 0.0025*ang_scale - 0.0025/9.
b1m.angle = 0.0014*ang_scale


b2.l = 0.2
d3.l = 0.63
b1m.l = 0.15


# different beta matching
b1.k1 = -0.8
b1m.k1 = -0.8
qd3.k1=  -0.8
qd2.k1=  -6.8
b0.k1 = -1.3
qf2a.k1 = 6.8
uq0.k1 = 6.7
uq0e.k1 = 6.7


A = 9 * b2.angle
b2_taper = 1.6 *  b2.angle
t_cof = b2_taper / 9.
a0 = (A - b2_taper * (9+1)/2.) / 9.


b2_1 = SBend(l=b2.l, angle=a0 + 1*t_cof)
b2_2 = SBend(l=b2.l, angle=a0 + 2*t_cof)
b2_3 = SBend(l=b2.l, angle=a0 + 3*t_cof)
b2_4 = SBend(l=b2.l, angle=a0 + 4*t_cof)
b2_5 = SBend(l=b2.l, angle=a0 + 5*t_cof)
b2_6 = SBend(l=b2.l, angle=a0 + 6*t_cof)
b2_7 = SBend(l=b2.l, angle=a0 + 7*t_cof)
b2_8 = SBend(l=b2.l, angle=a0 + 8*t_cof)
b2_9 = SBend(l=b2.l, angle=a0 + 9*t_cof)



A = 10 * b1m.angle
b1_taper = 0.0 *  b1m.angle
t_cof = b1_taper / 10.
a0 = (A - b1_taper * (10+1)/2.) / 10.


b1m_1 = SBend(l=b1m.l, angle=a0 + 1*t_cof, k1=b1m.k1)
b1m_2 = SBend(l=b1m.l, angle=a0 + 2*t_cof, k1=b1m.k1)
b1m_3 = SBend(l=b1m.l, angle=a0 + 3*t_cof, k1=b1m.k1)
b1m_4 = SBend(l=b1m.l, angle=a0 + 4*t_cof, k1=b1m.k1)
b1m_5 = SBend(l=b1m.l, angle=a0 + 5*t_cof, k1=b1m.k1)
b1m_6 = SBend(l=b1m.l, angle=a0 + 6*t_cof, k1=b1m.k1)
b1m_7 = SBend(l=b1m.l, angle=a0 + 7*t_cof, k1=b1m.k1)
b1m_8 = SBend(l=b1m.l, angle=a0 + 8*t_cof, k1=b1m.k1)
b1m_9 = SBend(l=b1m.l, angle=a0 + 9*t_cof, k1=b1m.k1)
b1m_10 = SBend(l=b1m.l, angle=a0 + 10*t_cof, k1=b1m.k1)



#w/o taper
be1 = (b1m,b1m,b1m,b1m,b1m,b1m,b1m,b1m,b1m,b1m)
#with taper
#be1 = (b1m_1,b1m_2,b1m_3,b1m_4,b1m_5,b1m_6,b1m_7,b1m_8,b1m_9,b1m_10)



block1 = (qf0,d10,be0,d10,qf1)

block0 = (qf0,d10,be0,d10,qf0)

# with taper
block3 =(qf1,d10,b1m_1,b1m_2,b1m_3,b1m_4,b1m_5,b1m_6,b1m_7,b1m_8,b1m_9,b1m_10,qd3,
        d2,qf2b,d4,sf1,d4,qf2a,d3,uq1, ud2, b2_1,b2_2,b2_3,b2_4,b2_5,b2_6,b2_7,b2_8,b2_9,d1,qd2, ud1,uq0, ud0)

# with canting

ud0_cant = Drift(l = 3.21-0.2)
bcant  = SBend(l = 0.2, angle=0.000*ang_scale)

block3 =(qf1,d10,b1m_1,b1m_2,b1m_3,b1m_4,b1m_5,b1m_6,b1m_7,b1m_8,b1m_9,b1m_10,qd3,
        d2,qf2b,d4,sf1,d4,qf2a,d3,uq1, ud2, b2_1,b2_2,b2_3,b2_4,b2_5,b2_6,b2_7,b2_8,b2_9,d1,qd2, ud1,uq0, ud0_cant, bcant)



block3e =(qf1,d10,b1m_1,b1m_2,b1m_3,b1m_4,b1m_5,b1m_6,b1m_7,b1m_8,b1m_9,b1m_10,qd3,
        d2,qf2b,d4,sf1,d4,qf2a,d3,uq1, ud2e, b2_1,b2_2,b2_3,b2_4,b2_5,b2_6,b2_7,b2_8,b2_9,d1,qd2e, ud1e,uq0e, ud0e)

celarc =(block3[::-1],block1[::-1],block1,block3)


lat = MagneticLattice(celarc)
