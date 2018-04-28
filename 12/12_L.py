# 12_L1
print('cddcc'[int(input())-1])

# 12_L2
class rint :
    def __init__(self, r):
        self.r = int(r[::-1])
    def __lt__(self, rhs):
        return self.r < rhs.r
    def __str__(self):
        return str(self.r)[::-1]
    def __int__(self):
        return self.r
    def __add__(self, rhs):
        return rint(str(self.r + rhs.r)[::-1])
t, r1, r2 = input().split()
a = rint(r1); b = rint(r2)
if t == '1' :       print(a < b)
elif t == '2' :     print(int(a),int(b))
elif t == '3' :     print(str(a),str(b))
elif t == '4' :     print(int(a + b))
else :          print(str(a + b))

# 12_L3
class Complex :
    def __init__(self,a,b):
        self.a, self.b = a, b
    def __str__(self):
        a, b = self.a, self.b
        if a == b == 0:     return '0'
        return '{}{}{}{}'.format(['', a][a!=0], ['-', '+'][b>0], \
            ['', abs(b)][b!=0 and abs(b)!=1], ['', 'i'][b!=0]).strip('+').rstrip('-')
    def __add__(self, rhs):
        return Complex(self.a+rhs.a, self.b+rhs.b)
    def __mul__(self, rhs):
        a, b, c, d = self.a, self.b, rhs.a, rhs.b
        return Complex(a*c-b*d, a*d+b*c)
    def __truediv__(self, rhs):
        a, b, c, d = self.a, self.b, rhs.a, rhs.b
        e = c**2 + d**2
        return Complex( (a*c+b*d)/e, (-a*d+b*c)/e )
t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 :         print(c1)
elif t == 2 :       print(c2)
elif t == 3 :       print(c1+c2)
elif t == 4 :       print(c1*c2)
else :          print(c1/c2)

# 12_L4 (fsum = float sum)
from math import fsum
class piggybank:
    def __init__(self):
        self.coins = {}
    def add(self, v, n):
        if sum(self.coins.values()) + n > 100:
            return False
        v = float(v)
        self.coins[v] = self.coins.get(v, 0) + n
        return True
    def __float__(self):
        return fsum(k*v for k, v in self.coins.items())
    def __str__(self):
        return '{' + ', '.join('{}:{}'.format(k, v) for k, v in sorted(self.coins.items())) + '}'
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1:      eval(c)
for c in cmd2:      eval(c)