# 01_V1 (simple)
answers = [ 'e', 'b', 'e', 'b', 'b' ]
n = int(input())
print(answers[n-1].lower())

# 01_V1 (Advance)
print('ebebb'[int(input())-1])

# 01_V2
from math import radians, sin
a = float(input())
b = float(input())
c = float(input())
print('area = ' + str(0.5 * a * b * sin(radians(c))) + ' (sq cm)')

# 01_V3
h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
t1 = h1*3600 + m1*60 + s1
t2 = h2*3600 + m2*60 + s2
dt = t2 - t1
dh = dt // 3600
dm = (dt - dh * 3600) // 60
ds = dt - dh * 3600 - dm * 60
print(str(dh) + ":" + str(dm) + ":" + str(ds))

# 01_V4
from math import sqrt, log
w = float(input())
h = float(input())
print(sqrt(w*h) / 60)
print(0.024265 * w ** 0.5378 * h ** 0.3964)
print(0.0333 * w ** (0.6157 - 0.0188 * log(w, 10)) * h ** 0.3)
