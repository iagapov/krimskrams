from ocelot import *
from ocelot.gui.accelerator import *
from ocelot.cpbd.chromaticity import *

np.set_printoptions(precision=2, suppress=True, linewidth=120)


from pylab import *

betay = 12.9327615792
betax = 1.40881394531
iidm = Matrix(rm13=-sqrt(betax/betay), rm24=-sqrt(betay/betax), rm31=sqrt(betay/betax), rm42=sqrt(betax/betay), l = 0.00001 )
machine = (iidm, Drift(l=0.00001))
lat = MagneticLattice( machine )
print lattice_transfer_map(lat, 5.0)
navi = Navigator()
t_maps = get_map(lat, lat.totalLen, navi, order=1)

for t in t_maps:
    print t, t.type
    print t.R(5.0)
    print np.linalg.det(t.R(5.0))


print 'element by element:'

R = np.eye(6)

for e in lat.sequence:
    print e.transfer_map(e.l).R(5.0)
    R = np.dot( e.transfer_map(e.l).R(5.0) ,  R )
    
print 'mul test:'
print  R