
from ocelot import *
from ocelot.gui.accelerator import *
from ocelot.cpbd.chromaticity import *



q1 = Quadrupole(l=0.2, k1 = -2, id='q1')
q2 = Quadrupole(l=0.2, k1 = 3, id='q2')
q3 = Quadrupole(l=0.2, k1 = -3, id='q3')


d1 = Drift(l=1)
d2 = Drift(l=2)
d3 = Drift(l=2)
d4 = Drift(l=2)


q1.k1 = -2.71718488757
q2.k1 = 3.28422035474
q3.k1 = -3.34077230645
d1.l= 0.803280163252
d2.l= 1.56461071843
d3.l= 1.95039529109


ms = Marker()
me = Marker()


c2t = (ms,d1,q1,d2,q2,d3,q3,d4, me)

t2c = (d4,q3,d3,q2,d2,q1,d1)


beam = Beam()
beam.E = 5.0

beam.beta_x  = 3.56457142227
beam.beta_y  = 11.5608486441
beam.alpha_x = -1.05603806184
beam.alpha_y = -1.26951045783


tw0 = Twiss(beam)

lat = MagneticLattice(c2t)

constr = {}
constr['global'] = {'beta_x':['<',38], 'beta_y':['<',38]}
constr[me] = {'alpha_x':0.0, 'alpha_y': 0.0, 'beta_x':3.0, 'beta_y': 3.0 }
#varz = [q1,q2,q3,q4,qf,qd, d1, d2, d3, d4]
varz = [q1,q2,q3,d1,d2,d3]
#match(lat, constr, varz, tw0, max_iter=5000, method='simplex')

print 'values:'
for v in varz:
    if v.__class__ in (Quadrupole, SBend): 
        print v.id, '=', v.k1
    if v.__class__ in (Drift,): 
        print v.id, 'l=', v.l

lat.update_transfer_maps() # need it since the lattice length was modified in matching

tws = twiss(lat, tw0,nPoints=101)
plot_opt_func(lat, tws, legend = False)

lat = MagneticLattice( (c2t, t2c) )

tws = twiss(lat, tw0,nPoints=101)
plot_opt_func(lat, tws, legend = False)


plt.show()




# variable names for lattice designer
__lattice__ = c2t
__beam__ = beam
__tws__ = Twiss(beam)
__knobs__ = None
__lattice_list__ = {'lss':(c2t, __tws__)}
 
