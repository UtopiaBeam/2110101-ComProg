# 02_P1
x = int(input())
if x > 0 :
    print('positive')
elif x < 0 :
    print('negative')
else :
    print('zero')
if x % 2 == 0 :
    print('even')
else :
    print('odd')

# 02_P2
x = float(input())
if 80 <= x <= 100 :
    print('A')
elif 75 <= x < 80 :
    print('B+')
elif 70 <= x < 75 :
    print('B')
elif 65 <= x < 70 :
    print('C+')
elif 60 <= x < 65 :
    print('C')
elif 55 <= x < 60 :
    print('D+')
elif 50 <= x < 55 :
    print('D')
elif 0 <= x < 50 :
    print('F')
else :
    print('ERROR')

# 02_P2 (Adv: list + next() + inline if-else + generator)
score = [0, 50, 55, 60, 65, 70, 75, 80, 100]
grade = ['ERROR', 'F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']
x = float(input())
print( next((gr for sc, gr in zip(score, grade) if x < sc or x == sc == 100), 'ERROR') )

# 02_P3
a, b, c = [int(x) for x in input().split()]
if a + b > c and b + c > a and c + a > b :
    print('YES')
else :
    print('NO')

# 02_P3 (Adv: inline if-else)
a, b, c = [int(x) for x in input().split()]
print('YES' if a + b > c and b + c > a and c + a > b else 'NO')

# 02_P4
from math import ceil
h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
dt = (h2 - h1) * 60 + (m2 - m1)
ans = 0
if dt <= 15 :
    ans = 0
elif 15 < dt <= 180 :
    ans = 10 * ceil(dt / 60)
elif 180 < dt <= 360 :
    ans = 30 + 20 * ceil((dt - 180) / 60)
else :
    ans =  200
print(ans)

# 02_P5
price = float(input())
coupon = input().strip()
card = input().strip()
discount = 0
if coupon == "Y":
    discount += 5
if card == "Y":
    if discount > 0:
        discount += 15
    else:
        discount += 10
print(price * ((100 - discount) / 100))

# 02_P6
a1, b1, c1 = [float(e) for e in input().split()]
a2, b2, c2 = [float(e) for e in input().split()]
if a1*b2 != a2*b1 :
    print('one solution')
elif b1*c2 != b2*c1 or a1*c2 != a2*c1 :
    print('no solution')
else :
    print('many solutions')

# 02_P7
tax = int(input())
ans = 0
if 1 <= tax :
    ans += min(tax, 100000) * 5 / 100
if 100000 < tax :
    ans += (min(tax, 500000) - 100000) * 10 / 100
if 500000 < tax :
    ans += (min(tax, 1000000) - 500000) * 20 / 100
if 1000000 < tax :
    ans += (min(tax, 4000000) - 1000000) * 30 / 100
if 4000000 < tax :
    ans += (tax - 4000000) * 37 / 100
print(ans)

# 02_P8 (Adv: inline if-else)
y = int(input()) - 543
print(29 if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else 28)

# 02_P9
m, y = [int(e) for e in input().split()]
y -= 543
if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12 :
    print(31)
elif m == 2 :
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 :
        print(29)
    else :
        print(28)
else :
    print(30)

# 02_P9 (Adv: list + inline if-else)
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m, y = [int(e) for e in input().split()]
y -= 543
print(month[m-1] + (1 if (m == 2 and (y % 4 == 0 and y % 100 != 0) or y % 400 == 0) else 0) )

# 02_P10 (Adv: list)
d, m, y = [int(x) for x in input().split()]
if m < 3 :
    m += 12
    y -= 1
c = y // 100
k = y % 100
w = (d + (26*(m+1))//10 + k + k//4 + c//4 + 5*c) % 7
print(['SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI'][w])

# 02_P11
x1, y1, r1, x2, y2, r2 = [float(x) for x in input().split()]
d = (x1 - x2) ** 2 + (y1 - y2) ** 2 - (r1 + r2) ** 2
if abs(d) < 1e-3 :
    print(1)
elif d < 0 :
    print(2)
else :
    print(3)

# 02_P12
A, a = [int(x) for x in input().split()]
B, b = [int(x) for x in input().split()]
b += a
a = 0
if b > B :
    a = b - B
    b = B
print(a, b)