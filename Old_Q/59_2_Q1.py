# 59_2_Q1_2_p (Adv: list)
d, m, y = (int(x) for x in input().split())
d, y = d+15, y-543
if m == 2 :     n = 29 if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0) else 28
else :          n = 31 if m in [1, 3, 5, 7, 8, 10, 12] else 30
if d > n :      d, m = d-n, m+1
if m > 12 :     m, y = m-12, y+1
print(d, m, y+543, sep = '/')

# 59_2_Q1_3_p
a, b, c = (float(e) for e in input().split())
t = b*b - 4*a*c
if t < 0 :          print('Roots are complex numbers')
elif a != 0 :
    tr1, tr2 = (-b-t**0.5)/(2*a), (-b+t**0.5)/(2*a)
    print('{:.2f}'.format(min(tr1, tr2)) + ('' if t == 0 else ' {:.2f}'.format(max(tr1, tr2))))
elif b != 0 :       print('{:.2f}'.format(-c/b))
elif c != 0 :       print('No roots exists')
else :              print('Roots are any numbers')

# 59_2_Q1_4_p
from math import sin, pi
t, mn = 0, [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d1, m1, y1, d2, m2, y2 = (int(x) for x in input().split())
y1, y2 = y1-543, y2-543
t += mn[m1] - d1 + sum(mn[m1+1:]) + (1 if m1 <= 2 and (y1 % 400 == 0 or (y1 % 4 == 0 and y1 % 100 != 0)) else 0)
t += d2 + sum(mn[:m2]) + (1 if m2 > 2 and (y2 % 400 == 0 or (y2 % 4 == 0 and y2 % 100 != 0)) else 0)
t += 365 * max(0, y2-y1-1)
print(t, '{:.2f} {:.2f} {:.2f}'.format(sin(2*pi*t/23), sin(2*pi*t/28), sin(2*pi*t/33)))