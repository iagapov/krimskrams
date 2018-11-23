# fodo lattice

from ocelot import *
from ocelot.gui.accelerator import *
from ocelot.cpbd.chromaticity import *
from pylab import *

from copy import deepcopy
from scipy.optimize import *


from fodo import *


beam = Beam()
beam.E = 5.0
'''
beam.beta_x = 9.46309318066
beam.beta_y = 2.72867802371
beam.alpha_x = -1.93123240939
beam.alpha_y = 0.605122378761
beam.Dx  = 0.440549263184
beam.Dxp = 0.0906141292549
'''

lat = MagneticLattice(cell)
tws0 = Twiss()
tws0.x = 0.1
tws=twiss(lat, tws0)
#plot_opt_func(lat, tws, top_plot = ["x", "y"], hold = False)
plot_opt_func(lat, tws, top_plot = ["mux", "muy"], hold = False)

tw0 = tws[0]

n = 1000

plist = []

for i in range(n):
    x, px = ellipse_from_twiss(15.e-5, tw0.beta_x, tw0.alpha_x)
    #y, py = ellipse_from_twiss(7.e-6, tw0.beta_y, tw0.alpha_y)
    y, py = 0., 0.
    plist.append(Particle(x=x, px=px, y=y, py=py))

figx = plt.figure('x')
axx = figx.add_subplot(111)
axx.plot([p.x for p in plist], [p.px for p in plist],'b.')
figy=plt.figure('y')
axy = figy.add_subplot(111)
axy.plot([p.y for p in plist], [p.py for p in plist],'b.')

'''
navi = Navigator()
navi.z0 = 0
dz = lat.totalLen / 17

while navi.z0 < lat.totalLen:
    track(lat, plist, dz=dz, navi=navi, order=2)
    #print navi.z0
    #axx.plot([p.x for p in plist], [p.px for p in plist],'r.', alpha = 0.2)
    #axy.plot([p.y for p in plist], [p.py for p in plist],'r.', alpha = 0.2)

axx.plot([p.x for p in plist], [p.px for p in plist],'r.')
axy.plot([p.y for p in plist], [p.py for p in plist],'r.')
'''

for i in range(150):
    print 'turn', i
    navi = Navigator()
    track(lat, plist, dz=lat.totalLen, navi=navi, order=2)

#track_nturns(lat, 1, plist, order=1)

axx.plot([p.x for p in plist], [p.px for p in plist],'g.')
axy.plot([p.y for p in plist], [p.py for p in plist],'g.')


between_sext = MagneticLattice( ( d2, B1, d3, d4, Q2, d5) )
R = lattice_transfer_map(between_sext, 5.0) 
print np.linalg.norm(R - eye(6))
print between_sext.totalLen


plt.show()
