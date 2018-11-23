'''
focusing triplet, collider-like
'''


from ocelot import *
from ocelot.gui.accelerator import *
from ocelot.cpbd.chromaticity import *



q1 = Quadrupole(l=0.2, k1 = -1.16, id='q1')
q2 = Quadrupole(l=0.2, k1 = 2.6, id='q2')
q3 = Quadrupole(l=0.2, k1 = -1.5, id='q3')
q4 = Quadrupole(l=0.2, k1 = 1.7, id='q4')

qf = Quadrupole(l=0.2, k1 = 1.7, id='qf')
qd = Quadrupole(l=0.2, k1 = -1.5, id='qd')


q1.k1 = -1.43901707307
q2.k1 = 2.78888482827
q3.k1 = -1.44427225283
q4.k1 = 1.79336370172
qf.k1 = 1.8784277055
qd.k1 = -1.60352185869


old_values = {}
knob = {}

for v in (q1,q2,q3,q4,qf,qd):
    old_values[v] = v.k1


d1 = Drift(l=1.17062264707)
d2 = Drift(l=0.801733628235)
d3 = Drift(l=4.31143677929)
d4 = Drift(l=5.39051978371)
d = Drift(l=5.)



ms = Marker()
me = Marker()


lss = (ms,d1,q1,d2,q2,d3,q3,d4,q4,d,qd,d,qf,d,qd,d,q4,d4,q3,d3,q2,d2,q1,d1, me)

beam = Beam()
beam.E = 5.0
beam.beta_x = 7.62327
beam.beta_y = 10.19622
beam.alpha_x = -2.60532
beam.alpha_y = -0.28820

tw0 = Twiss(beam)

lat = MagneticLattice(lss)

constr = {}
constr['global'] = {'beta_x':['<',38], 'beta_y':['<',38]}
constr[me] = {'beta_x':beam.beta_x, 'alpha_y':-beam.alpha_y, 'beta_y':beam.beta_y, 'alpha_y':-beam.alpha_y }
#varz = [q1,q2,q3,q4,qf,qd, d1, d2, d3, d4]
varz = [q1,q2,q3,q4,qf,qd]
#match(lat, constr, varz, tw0, max_iter=5000, method='simplex')

print 'values:'
for v in varz:
    if v.__class__ in (Quadrupole, SBend): 
        print v.id, '=', v.k1
    if v.__class__ in (Drift,): 
        print v.id, 'l=', v.l

lat.update_transfer_maps()

tws=twiss(lat, Twiss(beam), nPoints=100)

mux = tws[-1].mux
muy = tws[-1].muy

print ( mux, muy )


mux_new = mux + 0.1
muy_new = muy + 0.

constr = {}
constr[me] = {'beta_x':beam.beta_x, 'alpha_y':-beam.alpha_y, 'beta_y':beam.beta_y, 'alpha_y':-beam.alpha_y ,'mux':mux_new, 'muy':muy_new }
varz = [q1,q2,q3,q4, qf,qd]
#match(lat, constr, varz, tw0, max_iter=5000, method='simplex')

print 'values:'
for v in varz:
    if v.__class__ in (Quadrupole, SBend): 
        print v.id, '=', v.k1
        knob[v] = v.k1 - old_values[v]
    if v.__class__ in (Drift,): 
        print v.id, 'l=', v.l


tws=twiss(lat, Twiss(beam), nPoints=100)
plot_opt_func(lat, tws, legend = False)

#print(tws[0])
#print(tws[-1])


print 'dmux:', tws[-1].mux - mux
print 'dmuy:', tws[-1].muy - muy

for e in knob.keys():
    print e.id, '-->', knob[e]

plt.show()


mux_a = []
muy_a = []
a_a = []

'''
for a in linspace(-10, 10, 20):

    for v in (q1,q2,q3,q4,qf,qd):
        v.k1 = old_values[v] + a * knob[v]
    lat.update_transfer_maps()
    tws=twiss(lat, Twiss(beam), nPoints=100)
    a_a.append(a)
    mux_a.append(tws[-1].mux)
    muy_a.append(tws[-1].muy)
 

plt.figure()
plt.plot(a_a, mux_a, 'bd--')
plt.plot(a_a, muy_a, 'gd--')
plt.show()
'''


knob_mux = {}
knob_mux[q1] = -0.00596601955821
knob_mux[q2] = -0.000795885159465
knob_mux[qd] = -0.00298393106901
knob_mux[qf] = -0.0103114352294
knob_mux[q3] = 0.00342181853282
knob_mux[q4] = 0.0229556277793



north = (celarc*7, celarce, lss, celarcs, celarc*7)

# variable names for lattice designer
__lattice__ = lss
__beam__ = beam
__tws__ = Twiss(beam)

__lattice_list__ = {'lss':(lss, __tws__),'north':(north, None)}
 
__knobs__ = {'knob_mux':knob_mux}

