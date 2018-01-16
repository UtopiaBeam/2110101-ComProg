# 01_L1
answers = [ 'b', 'e', 'e', 'b', 'd' ]
n = int(input())
print(answers[n-1].lower())
# 01_L1 (Adv)
print('beebd'[int(input())-1])

# 01_L2
from math import radians, cos, sqrt
# Similar to "import math" but this command imports functions.
a = float(input())
b = float(input())
c = float(input())
print('c = ' + str(sqrt(a**2 + b**2 - 2*a*b*cos(radians(c)))) + ' cm.')

# 01_L3
h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2
dt = (t2 - t1 + 24*60*60) % (24*60*60)
dh = dt // (60*60)
dt -= dh * 60*60
dm = dt // 60
dt -= dm*60
ds = dt
print(str(dh) + ":" + str(dm) + ":" + str(ds))

# 01_L4


# 01_L4 (Adv)
n = int(input())
sum = 0
for i in range (2, 14) :
    sum += i * (n % 10)
    n //= 10
print((11 - sum % 11) % 10)
