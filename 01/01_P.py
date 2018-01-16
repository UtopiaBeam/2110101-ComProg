# 01_P1
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# 01_P2
r = float(input())
print(3.14159 * r * r)
# or
print(3.14159 * float(input()) ** 2)

# 01_P3 (Adv)
ans = 0
for i in range(5) :
    t = float(input())
    ans += t
print(ans / 5)

# 01_P4 (Adv)
x = float(input())
sum = 1 + x
for i in range(2, 5) :
    p = 1;  q = 1
    for j in range (1, i+1) :
        p *= x;     q *= j
    print(p / q)
    sum += p / q
print(sum)

# 01_P5
from math import sqrt
a = float(input())
b = float(input())
c = float(input())
root = sqrt(b**2-4*a*c)
x1 = (-b+root)/(2*a)
x2 = (-b-root)/(2*a)
print("x1 =", x1)
print("x2 =", x2)

# 01_P6
a1, b1, c1 = [float(e) for e in input().split()]
a2, b2, c2 = [float(e) for e in input().split()]
x = (b1*c2 - b2*c1) / (b2*a1 - b1*a2)
y = (a1*c2 - a2*c1) / (a2*b1 - a1*b2)
print(str(x) + ' ' + str(y))

# 01_P7
c = float(input())
f = 9/5 * c + 32
k = c + 273.15
print(str(f) + ' ' + str(k))

# 01_P8
w = int(input())
h = int(input())
h /= 100
print(w / (h*h))

# 01_P9
a, b, c = [int(e) for e in input().split()]
p = (a + b + c) / 2
ans = (p * (p-a) * (p-b) * (p-c)) ** 0.5
print(ans)

# 01_P10 (Adv)
n = input()
x = int(n)
sum = 0
for i in range (2, 11) :
    sum += i * (x % 10)
    x //= 10
print(n + str((11 - sum % 11) % 11))
