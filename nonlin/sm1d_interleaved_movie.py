'''
interleavoing 2 snandard maps, movie
'''

#from pylab import *


''' test mapping '''

from numpy import sin

def sm2(x0, y0, nt, a = 2.6, b=2.6, phi=0.0):

    x = x0
    y = y0
    xs = [x0,]
    ys = [y0,]

    cs = np.cos(phi)
    ss = np.sin(phi)

    for i in range(nt):
        y = mod(y  + a * sin(x), 2*pi)
        x = mod(x + y, 2*pi)

        x2 = x * cs + y * ss
        y2 = -x * ss + y * cs

        y2 = mod(y2  + b * sin(x2), 2*pi)
        x2 = mod(x2 + y2, 2*pi)

        x = x2
        y = y2

        xs.append(x)
        ys.append(y)

    #return np.array(xs), mod(np.array(ys) + pi, 2*pi)
    return np.array(xs), mod(np.array(ys), 2*pi)



def get_phase_space(phi=0.0):

    ai = 1.11
    bi = 1.91

    xa = None
    ya = None

    for x0 in np.linspace(0, 2*pi, 100):
        x, y = sm2(x0,0.0, 1000, a=ai, b=bi,  phi=phi)
        if xa is None:
            xa = x
            ya = (y + pi) % (2 * pi)
        else:
            xa = np.concatenate([xa, x])
            ya = np.concatenate([ya, (y + pi) % (2 * pi)] )

    return xa, ya




import numpy as np
import sys
from numpy import pi, sin, mod
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as manimation

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)

fig = plt.figure()
#l, = plt.plot([], [], 'k-o')

x0, y0 = get_phase_space(phi=0.0)

ax = fig.add_subplot(111)
ax.set_title(r"$\phi$={}".format(0.0))
l, = ax.plot(x0, y0, '.', color='black',alpha=0.1)

plt.xlim(pi-2., pi+2.)
plt.ylim(pi-2., pi+2.)


#x0, y0 = 0, 0

with writer.saving(fig, "c:/workspace/misc/mbo/writer_test_2.mp4", 300):
    nframes = 2000
    for i in range(nframes):
        phi = 0.00005*i
        ax.set_title(r"$\phi$={}".format(phi))
        print "{}% ready".format((100*i)/ nframes)
        x0, y0 = get_phase_space(phi=phi)
        l.set_data(x0, y0)
        writer.grab_frame()
