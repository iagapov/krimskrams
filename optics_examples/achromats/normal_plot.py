from pylab import *
import numpy.fft as fft


fname = 'c:/workspace/p4-t/madx/matching/normal_results.tfs'
#fname = 'c:/workspace/p4-m/normal_results.tfs'


import ocelot
from ocelot.adaptors.madx import TFS
tfs = TFS(fname)
print tfs.column_names

# specific for DQ
dq1 = np.array([0.0,0,0,0,0])
dq2 = np.array([0.0,0,0,0,0])
for i in range(len(tfs.column_values['NAME'])):
    print tfs.column_values['NAME'][i]
    if tfs.column_values['NAME'][i] == '"DQ1"':
        o = int(tfs.column_values['ORDER1'][i]) - 1
        value = float(tfs.column_values['VALUE'][i])
        dq1[o] = value
    if tfs.column_values['NAME'][i] == '"DQ2"':
        o = int(tfs.column_values['ORDER1'][i]) - 1
        value = float(tfs.column_values['VALUE'][i])
        dq2[o] = value

print dq1
print dq2

dp = np.linspace(-5.e-2, 5.e-2, 100)

print dp**2

q1 = dq1[0]*dp + dq1[1]*dp**2 + dq1[2]*dp**3 + dq1[3]*dp**4 + dq1[4]*dp**5
q2 = dq2[0]*dp + dq2[1]*dp**2 + dq2[2]*dp**3 + dq2[3]*dp**4 + dq2[4]*dp**5

ax1 = plt.figure().add_subplot(111)
p1, = ax1.plot(dp,q1,'b-', lw=2)
p2, = ax1.plot(dp,q2,'r-', lw=2)
#p2, = ax1.plot(tfs.column_values['Y'],'.--')
ax1.legend([p1,p2],['Q1','Q2'])
ax1.grid(True)

ax1 = plt.figure().add_subplot(111)
p1, = ax1.plot(q1,q2,'b-', lw=2)
ax1.grid(True)



#ax1.set_title(fname)
plt.show()
