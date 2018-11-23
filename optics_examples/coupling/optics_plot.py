from pylab import *
import numpy.fft as fft


fname = 'c:/workspace/optics_examples/coupling/ncell.tfs'


import ocelot
from ocelot.adaptors.madx import TFS



tfs = TFS(fname)
print tfs.column_names


'''
ax1 = plt.figure().add_subplot(111)
p1, = ax1.plot(tfs.column_values['X'],'.--')
p2, = ax1.plot(tfs.column_values['Y'],'.--')
ax1.legend([p1,p2],['X','Y'])
ax1.grid(True)
ax1.set_title(fname)
'''

ax2 = plt.figure().add_subplot(111)
p1, = ax2.plot(tfs.column_values['S'],tfs.column_values['BETA11'],'b-', lw=2)
p2, = ax2.plot(tfs.column_values['S'],tfs.column_values['BETA22'],'r-', lw=2)
ax2m = ax2.twinx()
p3, = ax2m.plot(tfs.column_values['S'],np.array(tfs.column_values['DISP1'])*1000.0,'g-', lw=2)
ax2.grid(True)
ax2m.grid(True)
ax2.legend([p1,p2,p3],['BETA11','BETA22','DISP1'])
ax2.set_title(fname)

ax3 = plt.figure().add_subplot(111)
p1, = ax3.plot(tfs.column_values['S'],tfs.column_values['BETA11P'],'b-', lw=2)
p2, = ax3.plot(tfs.column_values['S'],tfs.column_values['BETA22P'],'r-', lw=2)
ax3.grid(True)
ax3.legend([p1,p2],['BETA11P','BETA22P'])
ax3.set_title(fname)


plt.show()
