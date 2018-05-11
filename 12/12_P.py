# 12_P1
class ComplexNum:
    def __init__(self, re, im):
        self.re = re
        self.im = im
    def __str__(self):
        if self.im >= 0:
            return str(self.re) + '+' + str(self.im) + 'i'
        return str(self.re) + str(self.im) + 'i'
    def absolute(self):
        ab = (self.re**2+self.im**2)**0.5
        return round(ab, 2)
    def add(self,other):
        return ComplexNum(self.re+other.re, self.im+other.im)
    def conjugate(self):
        self.im *= -1
a, b, c, d = [int(e) for e in input().strip().split()]
complex1 = ComplexNum(a, b)
complex2 = ComplexNum(c, d)
con1 = ComplexNum(a, b)
con2 = ComplexNum(c, d)
con1.conjugate()
con2.conjugate()
print(complex1, con1, complex1.absolute())
print(complex2, con2, complex2.absolute())
print(complex1.add(complex2))

# 12_P2
def gcd(x, y):
    if x%y == 0: return y
    return gcd(y, x%y)
class Fraction:
    def __init__(self, a, b):
        self.numerator = a
        self.denominator = b
    def __str__(self):
        return '{}/{}'.format(self.numerator, self.denominator)
    def simplify(self):
        g = gcd(self.numerator, self.denominator)
        return Fraction(self.numerator//g, self.denominator//g)
    def add(self, other):
        return Fraction(self.numerator*other.denominator + self.denominator*other.numerator, self.denominator*other.denominator).simplify()
    def multiply(self, other):
        ans_numer = self.numerator * other.numerator
        ans_denom = self.denominator * other.denominator
        return Fraction(ans_numer,ans_denom).simplify()
a, b, c, d = [int(e) for e in input().strip().split()]
fraction1 = Fraction(a, b)
fraction2 = Fraction(c, d)
print(fraction1.add(fraction2))
print(Fraction.multiply(fraction1,fraction2))

# 12_P3
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return '({} {})'.format(self.value, self.suit)
    def getScore(self):
        if self.value.isdigit():    return int(self.value)
        elif self.value == 'A':     return 1
        else:       return 10
    def sum(self, other):
        return (self.getScore() + other.getScore()) % 10
    def __lt__(self, rhs):
        sc1, sc2 = 0, 0
        dc = {
                'A':    1,
                'J':    11,
                'Q':    12,
                'K':    13
            }
        if self.value.isdigit():    sc1 = int(self.value)
        else:       sc1 = dc[self.value]
        if rhs.value.isdigit():    sc2 = int(rhs.value)
        else:       sc2 = dc[rhs.value]
        return ((sc1+10)%13, self.suit) < ((sc2+10)%13, rhs.suit)
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])

# 12_P4
class Card:
    def __init__(self, value, suit):
        self.value, self.suit = value, suit
    def __str__(self):
        return '({} {})'.format(self.value, self.suit)
    def next1(self):
        val = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
        st = 'club diamond heart spade'.split()
        nx = [val.index(self.value), st.index(self.suit)+1]
        if nx[1] > 3:       nx = [(nx[0]+1)%13, 0]
        return Card(val[nx[0]], st[nx[1]])
    def next2(self):
        val = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
        st = 'club diamond heart spade'.split()
        nx = [val.index(self.value), st.index(self.suit)+1]
        if nx[1] > 3:       nx = [(nx[0]+1)%13, 0]
        self.value, self.suit = val[nx[0]], st[nx[1]]
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])

# 12_P5
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
class Rect:
    def __init__(self, p1, p2):
        self.lowerleft = p1
        self.upperright = p2
    def area(self):
        p1, p2 = self.lowerleft, self.upperright
        return (p2.x-p1.x) * (p2.y-p1.y)
    def contains(self, p):
        p1, p2 = self.lowerleft, self.upperright
        return (p1.x <= p.x <= p2.x) and (p1.y <= p.y <= p2.y)
x1, y1, x2, y2 = [int(e) for e in input().split()]
lowerleft = Point(x1, y1)
upperright = Point(x2, y2)
rect = Rect(lowerleft, upperright)
print(rect.area())
m = int(input())
for i in range(m):
    x,y = [int(e) for e in input().split()]
    p = Point(x, y)
    print(rect.contains(p))

# 12_P6
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "("+str(self.x) + "," + str(self.y) + ")"
class Rect:
    def __init__(self, p1, p2):
        self.lowerleft = p1
        self.upperright = p2
    def __str__(self):
        return str(self.lowerleft) + "-" + str(self.upperright)
    def area(self):
        p1, p2 = self.lowerleft, self.upperright
        return (p2.x-p1.x) * (p2.y-p1.y)
    def __lt__(self, rhs):
        return self.area() < rhs.area()
n = int(input())
rects = []
for i in range(n):
    x1, y1, x2, y2 = [int(e) for e in input().split()]
    rects.append(Rect(Point(x1,y1), Point(x2,y2)))
rects.sort()
for i in range(n):
    print(rects[i])

# 12_P7
class piggybank:
    def __init__(self):
        self.coin = {1:0, 2:0, 5:0, 10:0}
    def add1(self, n):
        self.coin[1] += n
    def add2(self, n):
        self.coin[2] += n
    def add5(self, n):
        self.coin[5] += n
    def add10(self, n):
        self.coin[10] += n
    def __int__(self):
        return sum(k*v for k, v in self.coin.items())
    def __lt__(self, rhs):
        return int(self) < int(rhs)
    def __str__(self):
        return '{' + ', '.join('{}:{}'.format(k, v) for k, v in sorted(self.coin.items())) + '}'
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)

# 12_P8 (Same as 12_L4)
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

# 12_P9
class rational:
    def __init__(self, n, d):
        self.n = n
        self.d = d
    def __str__(self):
        return str(self.n) + "/" + str(self.d)
    def __lt__(self, rhs):
        return float(self) < float(rhs)
    def __float__(self):
        return self.n / self.d
    def __add__(self, rhs):
        return rational( self.n*rhs.d + self.d*rhs.n, self.d*rhs.d )
    def __sub__(self, rhs):
        return rational( self.n*rhs.d - self.d*rhs.n, self.d*rhs.d )
    def __mul__(self, rhs):
        return rational( self.n*rhs.n, self.d*rhs.d )
    def __truediv__(self, rhs):
        return rational( self.n*rhs.d, self.d*rhs.n )
t, n1, d1, n2, d2 = input().split()
r1 = rational(int(n1),int(d1)); r2 = rational(int(n2),int(d2))
if t == '+' :   print(float(r1 + r2))
elif t == '-' : print(float(r1 - r2))
else :          print(float(r1 / r2))

# 12_P10
def gcd(x, y):
    return x if y == 0 else gcd(y, x%y)
class rational:
    def __init__(self, n, d):
        self.n = n
        self.d = d
    def __str__(self):
        GCD = gcd(self.n, self.d)
        return str(self.n//GCD) + "/" + str(self.d//GCD)
    def __lt__(self, rhs):
        return float(self) < float(rhs)
    def __float__(self):
        return self.n / self.d
    def __add__(self, rhs):
        return rational( self.n*rhs.d + self.d*rhs.n, self.d*rhs.d )
    def __sub__(self, rhs):
        return rational( self.n*rhs.d - self.d*rhs.n, self.d*rhs.d )
    def __mul__(self, rhs):
        return rational( self.n*rhs.n, self.d*rhs.d )
    def __truediv__(self, rhs):
        return rational( self.n*rhs.d, self.d*rhs.n )
t, n1, d1, n2, d2 = input().split()
r1 = rational(int(n1),int(d1)); r2 = rational(int(n2),int(d2))
if t == '+' : print(str(r1 + r2))
elif t == '-' : print(str(r1 - r2))
elif t == '/' : print(str(r1 / r2))
else : print(str(r1 * r2))