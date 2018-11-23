from bch import *
from pylab import *

A = Poly()
A[2,0] = -1.0 * 0.2
A[0,2] = -1.0 * 0.2

B = Poly()
B[2,0] = 1.0
B[0,2] = 1.0


x = Poly()
x[1,0] = 1.0

px = Poly()
px[0,1] = 1.0


vxs = []
vps = []
Is = []
xn, pxn = x, px
In = B

for i in range(0,20000):
    xn  = lexp(A,xn,n=15)
    pxn =  lexp(A,pxn,n=15)
    In =  lexp(A,In,n=30)
    vxs.append( xn((1,0)) )
    vps.append( pxn((1,0)) )
    #print(xn)
    Is.append( In( (1,1) ))
    #print(xn((1,0)))


plt.plot(vxs, vps,'.')
#plt.plot(Is, '-.')
plt.show()


'''
A = Poly()



e44 = []
t=np.linspace(0.0,pi, 50)
for mu in np.linspace(0.0,pi, 50):
    A[2,0] = 1.0 * mu / 2.
    A[0,2] = 1.0 * mu / 2.
    print(A)
    B = Poly()
    B[3,0] = 1.0
    print(B)

    E = bch(B,A)
    E = bch(E,B)
    print('exp(:A:)exp(:B:)=exp(:',E,':)')
    print(E[4,0])
    e44.append(E[3,0])

plt.plot(t/ (pi), e44)
plt.show()
'''
