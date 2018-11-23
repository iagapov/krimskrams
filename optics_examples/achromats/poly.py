from pylab import *

class Poly:
    def __init__(self, symbols = ()):
        self.f =  {}
        self.symbols = symbols
    
    def simplify(self):
        pass
    
    def __mul__(self, p):
        p2 = Poly(self.symbols)
        klmn1 = sorted(self.f.keys())
        klmn2 = sorted(p.f.keys())
        
        for i1 in klmn1:
            for i2 in klmn2:
                i3 = array(i1) + array(i2)
                #print 'monomial', i1,i2, i3
                if tuple(i3) in p2.f.keys(): 
                    p2.f[tuple(i3)] += self.f[i1]*p.f[i2]
                else:
                    p2.f[tuple(i3)] = self.f[i1]*p.f[i2]
        
        return  p2
    
    def D(self,sym):
        return diff(self,sym)
    
    def __add__(self,p):
        p2 = Poly(self.symbols)
        klmn1 = sorted(self.f.keys())
        klmn2 = sorted(p.f.keys())
        
        for i1 in klmn1:
            if i1 not in klmn2:
                p2.f[i1] = self.f[i1]
            else:
                p2.f[i1] = self.f[i1] + p.f[i1]
            
        for i2 in klmn2:
            if i2 not in klmn1:
                p2.f[i2] = p.f[i2]
        
        return p2


    def __sub__(self,p):
        return self.__add__(-p)

    def __neg__(self):
        p2 = Poly(self.symbols)
        for i in sorted(self.f.keys()):
            p2.f[i] = -self.f[i]
        return p2

    
    def __str__(self):
        print_tol = 1.e-10
        s = ''
        klmn = sorted(self.f.keys())

        for i in klmn:
            if abs(self.f[i]) < print_tol: continue
            
            if self.f[i] >= 0 and i != klmn[0]: 
                s += ' + '
            s += str(self.f[i])
            for j in range(len(self.symbols)):
                if i[j] > 1 : s = s +  self.symbols[j] + '^' + str(i[j])
                if i[j] == 1 : s = s +  self.symbols[j] 
             
        if len(s) < 1: s = '0.0'   
        return s
    
    
def diff(p,sym):
    p1 = Poly()
    p1.symbols = p.symbols
    idx = p.symbols.index(sym)
    #print 'sym idx', idx
    klmn = sorted(p.f.keys())
    for i in klmn:
        #print 'checking ', i
        klmn_d = ()
        for j in range(len(i)):
            #print j
            if j == idx:
                #print 'klmn', klmn_d, klmn_d[idx]
                klmn_d += (i[idx] - 1,)            
            else:
                klmn_d += (i[j],)
        #print 'diff order', klmn_d
        if -1 not in klmn_d:
            p1.f[klmn_d] = p.f[i] * i[idx]


    return p1

def grad(p):
    return [diff(p,s) for s in p.symbols]
    g = []
    for s in p.symbols: g.append(diff(p,s))
    


def PoissonBracket(f,g, canon):
    p2 = Poly(f.symbols)
    for iv in  canon:
        p2 = p2 + f.D(iv[0])*g.D(iv[1]) - f.D(iv[1])*g.D(iv[0])
    return p2

def PB(f,g,canon):
    return PoissonBracket(f,g, canon)

'''
tests
'''

def test_diff():
    p = Poly()
    p.symbols = ('x','y')
    
    p.f[(0,0)] = 1.0
    p.f[(1,0)] = 1.1
    p.f[(0,1)] = -4.5
    p.f[(3,2)] = 1.5
    p.f[(2,0)] = 1125
    p.f[(1,4)] = -1125
    p.f[(7,8)] = -0.1
    
    print 'polynomial:', p
    p1 = diff(p,'x')
    print 'diff:', p1
    print 'diff:', diff(diff(p1,'x'),'x')
    print p1.D('x')
    d = grad(p1)
    print 'grad', d[0], ';', d[1]

    #print p1.f


def test_mul():
    p1 = Poly(('x','y'))
    
    p1.f[(1,0)] = 1.0
    p1.f[(0,1)] = -1.0
    print p1
    
    
    p2 = Poly(('x','y'))
    
    p2.f[(1,0)] = 1.0
    p2.f[(0,1)] = 1.0
    p2.f[(1,1)] = 2.0
    print p2
    
    p3 = p1 * p2
    
    print 'p1*p2:', p3

def test_add():
    p1 = Poly(('x','y'))
    p1.f[(0,1)] = -2
    p2 = Poly(('x','y'))
    p2.f[(1,0)] = -3
    
    print p1
    print p2
    print 'p1+p2=', p1+p2

    p1 = Poly(('x','px','y','py'))
    p1.f[(1,0,0,0)] = 1
    p2 = Poly(('x','px','y','py'))
    p2.f[(1,0,0,0)] = -2
    
    p2.f[(1,2,0,1)] = 43
    
    print p1
    print p2
    print p1,'+++', p2, '=',p1+p2
    print p1,'---', p2, '=',p1-p2


def test_PB():

    f = Poly(('x','px'))
    f.f[(2,0)] = 0.5
    f.f[(0,2)] = 0.5
    g = Poly(('x','px'))
    g.f[(2,0)] = 0.5
    g.f[(0,2)] = 0.5

    print f, ';', g
    print PB(f,g, (('x','px'),))
    
    
f = Poly(('x','px'))
f.f[(2,0)] = 0.5
f.f[(0,2)] = 0.5
g = Poly(('x','px'))
g.f[(0,1)] = 1.0

print f, ';', g
print PB(g,f, (('x','px'),))
