from pylab import *


psi = np.linspace(0, 2*pi, 100)

D = 0.01
e = 0.1

J1 = 4. * (D + 1/2. * e* cos(psi))

D = 0.06
e = 0.1

J2 = 4. * (D + 1/2. * e* cos(psi))

D = 0.2
e = 0.1

J3 = 4. * (D + 1/2. * e* cos(psi))




ax = plt.subplot(111, projection='polar')
ax.plot(psi, J1, color='r', linewidth=3)
ax.plot(psi, J2, color='g', linewidth=3)
ax.plot(psi, J3, color='b', linewidth=3)
#ax.set_rmax(0.3)
ax.grid(True)
ax.set_title("A line plot on a polar axis", va='bottom')

#plt.figure()
#plt.plot(psi, J)

plt.show()
