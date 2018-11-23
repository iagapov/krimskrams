# Lie map stuff
from scipy.misc import factorial as fact

# (x,px) polynomial
class Poly:
    def __init__(self,n=2):
        self.n = n
        self.tol = 1.e-20 # anything below this rounded to zero
        self.coef = {}

    def __add__(self, B):
        C = Poly()
        b_marked = {}
        for i in self.coef.keys():
            if i in B.coef.keys():
                C[i] = self[i] + B[i]
                b_marked[i] = True
            else:
                C[i] = self[i]

        for i in B.coef.keys():
            if i not in b_marked.keys():
                C[i] = B[i]

        return C

    def __sub__(self, B):
        C = Poly()
        b_marked = {}
        for i in self.coef.keys():
            if i in B.coef.keys():
                C[i] = self[i] - B[i]
                b_marked[i] = True
            else:
                C[i] = self[i]

        for i in B.coef.keys():
            if i not in b_marked.keys():
                C[i] = -B[i]

        return C

    def __mul__(self, B):
        C = Poly()
        #print('mult')
        for i in self.coef.keys():
            i1, i2 = i
            v1 = self.coef[i]
            #print(i1, i2, '->', v1)
            for j in B.coef.keys():
                j1, j2 = j
                v2 = B.coef[j]
                k1, k2 = i1+j1, i2+j2
                v = v1*v2
                if (k1,k2) in C.coef.keys():
                    C[k1,k2] += v1*v2
                else:
                    C[k1,k2] = v1*v2
        return C

    # left mul by scalar
    def __rmul__(self,b):
        C = Poly()
        for i in self.coef.keys():
            C[i] = self[i] * b
        return C


    def __str__(self):
        st = "P="
        #return str(self.coef)
        for i in self.coef.keys():
            #if abs(self.coef[i]) < self.tol: continue
            if i[0] == 0 and i[1] == 0:
                st += (str(self.coef[i]) + '   ')
            if i[0] != 0 and i[1] == 0:
                st += (str(self.coef[i]) + 'x^' + str(i[0])  + '   ')
            if i[0] == 0 and i[1] != 0:
                st += (str(self.coef[i]) + 'px^'+str(i[1]) + '   ')
            if i[0] != 0 and i[1] != 0:
                st += (str(self.coef[i]) + 'x^' + str(i[0]) + '*px^'+str(i[1]) + '   ')


        return st

    def __getitem__(self,key):
        return self.coef[key]
    def __setitem__(self,key,val):
        self.coef[key] = val
    def __call__(self, val):
        v = 0.0
        for i in self.coef.keys():
            v += self.coef[i] *val[0]**(i[0]) * val[1]**(i[1])

        return v

#polynomial derivative (d_dx, d_dpx)
def d(A):
    C1=Poly()
    C2=Poly()
    for i in A.coef.keys():
        i1,i2 = i
        if i1>0: C1[i1-1,i2] = i1*A[i1,i2]
        if i2>0: C2[i1,i2-1] = i2*A[i1,i2]
    return C1, C2

# Poisson bracket
def pb(A,B):
    C1,C2 = d(A)
    D1,D2 = d(B)
    E = C1*D2 - C2*D1
    return E

# computes the polynomial h in the representation exp(:h:) = exp(:f:)exp(:g:)
#5th order explicit calculation
def bch(f,g):
    h = Poly()
    h = f + g +  0.5*pb(f,g)
    h = h + 1./12. * pb(f,pb(f,g)) + 1./12. * pb(g,pb(g,f)) + 1./24. * pb(f,pb(g,pb(g,f)))
    h = h - 1./720. * pb(g, pb(g, pb(g,pb(g,f)))) -1./720. * pb(f, pb(f, pb(f,pb(f,g))))
    h = h + 1./360. * pb(g, pb(f, pb(f,pb(f,g)))) +1./360. * pb(f, pb(g, pb(g,pb(g,f))))
    h = h + 1./120. * pb(f, pb(f, pb(g,pb(g,f)))) +1./120. * pb(g, pb(g, pb(f,pb(f,g))))
    return h

# evaluates exponential exp(:f:)g
def lexp(f,g, n=1):
    F = g
    u = g
    #print('debug exp:',u)
    for i in range(1,n):
        F = pb(f,F)
        u = u + 1./fact(i) * F
        #print('debug exp:',u)
    return u


def test_mul():
    A = Poly()
    A[2,0] = 1.0
    A[0,2] = -1.1
    B = Poly()
    B[2,0] = 1.1
    B[0,2] = 1.3
    B[13,18] = 0.5
    C = A*B
    D = -0.5 * B
    print(A)
    print(B)
    print(C)
    print(D)

def test_d():
    A = Poly()
    A[2,0] = 2.0
    A[11,12] = 2.5
    A[0,2] = -1.1
    print(A)
    C1,C2 = d(A)
    print('d/dx',C1)
    print('d/dpx',C2)

def test_add():
    A = Poly()
    A[2,0] = 0.5
    A[0,2] = 0.5
    A[1,1] = -7.0
    print(A)
    B = Poly()
    B[2,0] = 0.7
    B[0,2] = 0.9
    B[0,3] = 18.0
    print(B)

    E = A + B
    print('A+B:',E)

    E = A - B
    print('A-B:',E)


def test_pb():
    A = Poly()
    A[2,0] = 1.0
    A[0,2] = 0.0
    print(A)
    B = Poly()
    B[2,0] = 1.0
    B[0,2] = 0.0
    print(B)

    E = pb(A,B)
    print('[A,B]',E)

def test_bch():
    A = Poly()
    A[2,0] = 1.0
    A[0,2] = 1.0
    A[1,1] = 2.0
    print(A)
    B = Poly()
    B[2,0] = 1.0
    B[0,2] = 1.0
    print(B)

    E = bch(A,B)
    print('exp(:A:)exp(:B:)=exp(:',E,':)')

def test_bch_2():
    A = Poly()
    A[2,0] = 1.0
    A[0,2] = 1.0
    print(A)
    B = Poly()
    B[3,0] = 15.0
    print(B)

    E = bch(A,B)
    print('exp(:A:)exp(:B:)=exp(:',E,':)')


def test_lexp():
    A = Poly()
    A[2,0] = -1.0
    A[0,2] = -1.0
    B = Poly()
    B[1,0] = 1.0
    C = Poly()
    C[0,1] = 1.0

    D = Poly()
    D[0,2] = 1.0
    D[2,0] = 1.0


    print('A=',A)
    print('B=',B)
    print('C=',C)
    print('D=',D)

    E1 = lexp(A,B,n=15)
    E2 = lexp(A,C,n=15)
    E3 = lexp(A,D)
    print('exp(:A:)B=',E1)
    print('exp(:A:)C=',E2)

    print('det:',E1[1,0]*E2[0,1] - E1[0,1]*E2[1,0])

    print('exp(:A:)D=',E3)

def test_call():
    A = Poly()
    A[2,0] = 2.0
    A[0,2] = 2.0
    A[1,1] = 1.0

    print ( A((2,-2)) )


#test_call()
#test_lexp()
