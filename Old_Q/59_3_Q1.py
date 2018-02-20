# 59_3_Q1_2_p
a, b, c, d = map(int, input().split())
if a > b :
    a, b = b, a
    if d < a :      c += a
    elif c > d :    c -= a
    b = a + c + d
else :
    if c > a >= b :   d += a
    if d <= c :       b *= 2
    elif d % 2 == 0:    b += 2    
print(a, b, c, d)

# 59_3_Q1_3_p
from math import sqrt, tan, radians
a, n = float(input()), int(input())
if n == 3 :         print(round(sqrt(3)/4 * a * a, 3))
elif n == 4 :       print(round(a * a, 3))
elif n == 5 :       print(round(sqrt(5 * (5+2*sqrt(5))) * a * a / 4, 3))
elif n == 6 :       print(round(3*sqrt(3)/2 * a * a, 3))
elif n == 7 :       print(round(7*a*a/4 * 1/tan(radians(180)/7), 3))
else :              print('N/A')

# 59_3_Q1_4_p (Adv: list)
ls = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d, m, y = map(int, input().split())
op = input().strip()
y -= 543
ls[2] += 1 if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0) else 0 
if y + 543 < 2558 :         print('Invalid year')
elif not 1 <= m <= 12 :     print('Invalid month')
elif not 1 <= d <= ls[m] :  print('Invalid date')
elif op not in 'EQNF' :     print('Invalid delivery type')
else :
    if op == 'E' :      d += 1
    if op == 'Q' :      d += 3
    if op == 'N' :      d += 7
    if op == 'F' :      d += 14
    if d > ls[m] :      d, m = d-ls[m], m+1
    if m > 12    :      m, y = m-12, y+1
    print('delivered on {}/{}/{}'.format(d, m, y+543))

# 59_3_Q1_4_p (Adv: list + dict)
ls = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dc = { 'E' : 1, 'Q' : 3, 'N' : 7, 'F' : 14 }
d, m, y = map(int, input().split())
op = input().strip()
y -= 543
ls[2] += 1 if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0) else 0 
if y + 543 < 2558 :         print('Invalid year')
elif not 1 <= m <= 12 :     print('Invalid month')
elif not 1 <= d <= ls[m] :  print('Invalid date')
elif op not in 'EQNF' :     print('Invalid delivery type')
else :
    d += dc[op]
    if d > ls[m] :      d, m = d-ls[m], m+1
    if m > 12    :      m, y = m-12, y+1
    print('delivered on {}/{}/{}'.format(d, m, y+543))