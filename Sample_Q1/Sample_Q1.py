# Sample_Q1_1
from math import acos, pi, sqrt, pow
r, g, b = (float(input()) for _ in range(3))
h = 2*pi - acos( (2*r - g - b) / (2*sqrt( pow(r-g, 2) + (r-b)*(g-b))) )
s, i = 1 - 3*r / (r+g+b), (r+g+b) / 3
print(h, s, i, sep = '\n')


# Sample_Q1_2
a, b, c = (int(x) for x in input().split())
d = 0
if a != 0 and (b % a == 0 or c % a != 0) :
    d = b//a + c%a
else :
    d = int(input())
if d < b :
    a, b, c = c, 2*b, a
    if b > a+c :
        d, c = d + b//2, c-1
if d < b and d % 2 == 0 :
    a, c = a+b-d, c+1
elif d == b :
    a -= 1
elif d > a+c :
    b **= 2
else :
    d += b
print(a, b, c, d)

# Sample_Q1_3
from math import ceil
n = float(input())
if n < 0 :          print('ERROR')
else :
    n = ceil(n)
    if n <= 1.0 :       print(35.0)
    elif n <= 10 :      print(35.0 + 5.5*(n-1))
    elif n <= 20 :      print(35.0 + 5.5*9 + 6.5*(n-10))
    elif n <= 40 :      print(35.0 + 5.5*9 + 6.5*10 + 7.5*(n-20))
    elif n <= 60 :      print(35.0 + 5.5*9 + 6.5*10 + 7.5*20 + 8.0*(n-40))
    elif n <= 80 :      print(35.0 + 5.5*9 + 6.5*10 + 7.5*20 + 8.0*20 + 9.0*(n-60))
    else :          print(35.0 + 5.5*9 + 6.5*10 + 7.5*20 + 8.0*20 + 9.0*20 + 10.5*(n-80))

# Sample_Q1_3 (Adv: list)
ans, ls = 0, [(1, 35.0), (10, 5.5), (20, 6.5), (40, 7.5), (60, 8.0), (80, 9.0), (float('inf'), 10.5)]
n, p = float(input()), 0
if n < 0 :      print('ERROR')
else :
    n = __import__('math').ceil(n)
    for ds, cs in ls :
        ans, p = ans + max(0, cs * (min(n, ds) - p)), ds
    print(ans)

# Sample_Q1_4
n, m = (int(x) for x in input().split())
n, t = n // 10**m, (n // 10**(m-1)) % 10
if t > 5 or (t == 5 and n % 2 == 1) :
    n += 1
n *= 10**m
print(n)

# Sample_Q1_4 (Adv: round())
n, m = (int(x) for x in input().split())
print(round(n // 10**(m-1) / 10) * 10**m)