# need to rememberr

from ocelot.gui.accelerator import *
import ocelot
from ocelot import *
from pylab import *



from copy import deepcopy
from scipy.optimize import *

D0 = Drift (l = 0., eid = "D0")
D1 = Drift (l = 1.49, eid = "D1")
D2 = Drift (l = 0.1035, eid = "D2")
D3 = Drift (l = 0.307, eid = "D3")
D4 = Drift (l = 0.33, eid = "D4")
D5 = Drift (l = 0.3515, eid = "D5")
D6 = Drift (l = 0.3145, eid = "D6")
D7 = Drift (l = 0.289, eid = "D7")
D8 = Drift (l = 0.399, eid = "D8")
D9 = Drift (l = 3.009/2., eid = "D9")

SF = Sextupole(l = 0, k2 = 1.7673786254063251, eid = "SF")
SD = Sextupole(l = 0, k2 = -3.6169817233025707, eid = "SD")


Q1 = Quadrupole (l = 0.293, k1 = 2.62, eid = "Q1")
Q2 = Quadrupole (l = 0.293, k1 = -3.1, eid = "Q2")
Q3 = Quadrupole (l = 0.327, k1 = 2.8, eid = "Q3")
Q4 = Quadrupole (l = 0.291, k1 = -3.7, eid = "Q4")
Q5 = Quadrupole (l = 0.391, k1 = 4.0782, eid = "Q5")
Q6 = Quadrupole (l = 0.291, k1 = -3.534859, eid = "D6")

B1 = SBend(l = 0.23, angle = 0.23/19.626248, eid  = "B1")
B2 = SBend(l = 1.227, angle = 0.1227/4.906312, eid = "B2")

#und = Undulator (nperiods=200,lperiod=0.07,Kx = 0.49, id = "und")
#und.field_map.units = "mm"
#und.ax = 0.05
#M1 = Monitor(id = "m1")
#H1 = Hcor(l = 0.0, angle = 0.00, id = "H1")
#V2 = Vcor(l = 0.0, angle = 0.00, id = "V2")


superperiod = ( D9,Q6,D8,Q5,D7,Q4,D6,B1,B2,D5,Q3,D5,B2,B1,D4,SD,D2,Q2,D3,Q1,D2,SF,D1,D1,SF, D2,Q1,D3, Q2,D2,SD,D4,B1,B2,D5,Q3,D5,B2,B1,D6,Q4,D7,Q5,D8,Q6,D9)



m1 = Monitor(eid="start")
m2 = Monitor(eid="end")

dba = (m1,superperiod,m2)

beam = Beam()
beam.E = 6.0
beam.sigma_E = 0.002
beam.beta_x = 9.03267210229
beam.beta_y = 0.573294833302

lat = MagneticLattice(dba)
tw0 = Twiss(beam)
tws=twiss(lat, tw0, nPoints = 1000)
plot_opt_func(lat, tws, legend = False)


eb = EbeamParams(lat, beam, nsuperperiod=1)
print(eb)

#print(eb.integrals_id())
#print (eb.I5, eb.I2,eb.I4)
#print ( (6000.0 / 0.511)**2 * 0.383 * eb.I5 / (eb.I2 - eb.I4) )


plt.show()
