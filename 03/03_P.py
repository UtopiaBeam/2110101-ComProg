# 03_P1
n = int(input())
ans = 1
for i in range(1, n+1) :
    ans *= i
print(ans)

# 03_P1 (factorial())
from math import factorial
print(factorial(int(input())))

# 03_P2 (Adv: recursive function)
def f(n) :
    return 1 if n < 2 else n * f(n-1)
n, r, t = [int(x) for x in input().split()]
if t == 1 :
    print(f(n) // f(n-r))
else :
    print(f(n) // (f(n-r) * f(r)))

# 03_P3
n = int(input())
ans = 0
for i in range(1, n) :
    if i % 3 == 0 or i % 5 == 0 :
        ans += i
print(ans)

# 03_P4
n = int(input())
ans = 0
for _ in range(n) :
    ans += float(input())
print('No Data' if n == 0 else ans / n)

# 03_P5
ans = 0
n = 0
while True :
    tmp = float(input())
    if tmp < 0 :
        print('No Data' if n == 0 else ans / n)
        break
    else :
        ans += tmp
        n += 1

# 03_P6 (Adv: list + next() + generator)
score = [0, 50, 55, 60, 65, 70, 75, 80, 100]
grade = ['Error', 'F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']
while True :
    x = int(input())
    if x < 0 :
        break
    print( next((gr for sc, gr in zip(score, grade) if x < sc or x == sc == 100), 'Error') )

# 03_P7
n, x = [int(e) for e in input().split()]
cnt = 0
for _ in range(n) :
    t = int(input())
    if x == t :
        cnt += 1
print(cnt)

# 03_P8
n = int(input())
mx = 0
for a in range(1, n) :
    for b in range(a, n) :
        if a + b >= n :
            break
        if a**2 + b**2 == (n-a-b)**2 :
            mx = max(mx, n-a-b)
print(mx)

# 03_P9
a, b, c, xi, d = [float(e) for e in input().split()]
n = 1
while True :
    xf = xi - (a*(xi**2) + b*xi + c) / (2*a*xi + b)
    if abs(xf - xi) <= d :
        print(n)
        break
    n += 1
    xi = xf
    
# 03_P10 (Adv: list)
n = int(input())
ans = []
for i in range(n-1, 1, -1) :
    if n % i == 0 :
        ans += [i]
if len(ans) == 0 :
    print('Prime Number')
else :
    print(*ans)

# 03_P10 (Adv: list comprehension)
n = int(input())
ls = [x for x in range(n-1, 1, -1) if n % x == 0]
print(*ls if len(ls) > 0 else 'Prime Number')

# 03_P11
n = int(input())
p = [2]
if n < 0 :
    print('input unavailable')
elif n < 2 :
    print('none')
else :
    for i in range(3, n+1, 2) :
        for j in range(2, i) :
            if i % j == 0 :
                break
            if j == i-1 :
               p.append(i)
    print(*p)

# 03_P11 (Adv: set comprehension + Sieve of Eratosthenes)
from math import sqrt, ceil
n = int(input())
np = {j for i in range(2, int(ceil(sqrt(n)))) for j in range(2*i, n+1, i)}
p = [x for x in range(2, n+1) if x not in np]
if n < 0 :
    print('input unavailable')
else :
    print(*p if len(p) > 0 else 'none')

# 03_P12 (Adv: set comprehension + Sieve of Eratosthenes) 
from math import sqrt, ceil
n = int(input())
np = {j for i in range(2, int(ceil(sqrt(n)))) for j in range(2*i, n+1, i)}
p = [x for x in range(2, n+1) if x not in np]
ans = [x for x in p if n % x == 0]
print(*ans)

# 03_P13
r, c = [int(x) for x in input().split()]
for i in range(1, r+1) :
    for j in range(1, c+1) :
        print(i*j, end = ' ')
    print()

# 03_P13 (Adv: generator comprehension)
r, c = [int(x) for x in input().split()]
for i in range(1, r+1) :
    print(*(x*i for x in range(1, c+1)))

# 03_P14
n, op = (int(e) for e in input().split())
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if op == 1 and i <= j :     print('({},{})'.format(i, j))
        if op == 2 and i >= j :     print('({},{})'.format(i, j))
        if op == 3 and i+j == n+1 : print('({},{})'.format(i, j))

# 03_P14 (Adv: map() + lambda function + format() + escape character)
n, op = map(int, input().split())
f = [lambda i, j : i >= j, 
     lambda i, j : i <= j,
     lambda i, j : i + j == n + 1][op-1]
print(*('({},{})'.format(i, j)
    for i in range(1, n+1)
    for j in range(1, n+1)
    if f(i, j)), sep = '\n')

# 03_P15
n = int(input())
for i in range(n//2 - 1, -1, -1) :
    print('.'*i + '#'*(n-2*i) + '.'*(2*i+1) + '#'*(n-2*i) + '.'*i)
for _ in range(n//2 - 2) :
    print('#'*(2*n+1))
for i in range(n + 1) :
    print('.'*i + '#'*(2*n+1-2*i) + '.'*i)

# 03_P16
x = int(input())
y = int(input())
for i in range(1, y+1) :
    print('{} {} {}'.format(x, i, x*i))