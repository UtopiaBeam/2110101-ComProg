# 03_V1
print(['a', 'p', 'j', 'rs', 'v'][int(input()) - 1])

# 03_V2
sum = 0
while True :
    x = int(input())
    if x < 0 :
        break
    elif x % 2 == 0 :
        sum += x
print(sum)

# 03_V3
n = int(input())
chk = True
for x in range(n) :
    for y in range(x, n) :
        if x**2 + y**2 == n :
            print(x, y)
            chk = False
if chk :
    print('No solution')


# 03_V4
from math import pow
x = float(input())
ans = 0
k = 0
while True :
    fact = 1
    for i in range(1, 2*k+1) :
        fact *= i
    tmp = (pow(-1, k) * pow(x, 2*k)) / fact
    if abs(tmp) < 1e-8 :
        break
    ans += tmp
    k += 1
print(ans, k-1)

# 03_V4 (Adv: recursive function)
from math import pow
x = float(input())
ans = 0
k = 0
def fact(n) :
    return 1 if n < 2 else n * fact(n-1)
while True :
    tmp = (pow(-1, k) * pow(x, 2*k)) / fact(2*k)
    if abs(tmp) < 1e-8 :
        break
    ans += tmp
    k += 1
print(ans, k-1)