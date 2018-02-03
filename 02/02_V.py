# 02_V1
answers = [ 'a', 'e', 'e', 'b', 'c' ]
n = int(input())
print(answers[n-1].lower())

# 02_V1 (Adv)
print('aeebc'[int(input())-1])

# 02_V2
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a > b :
    a, b = b, a
if b > c :
    b, c = c, b
if c > d :
    c, d = d, c
if a > b :
    a, b = b, a
if b > c :
    b, c = c, b
if a > b :
    a, b = b, a
print(a, b, c, d)

# 02_V2 (Adv: sorted() + list comprehension)
print(*sorted([int(input()) for _ in range(4)]))

# 02_V3
d = float(input())
max = d
min = d
d = float(input())
if d > max :
    max = d
if d < min :
    min = d
d = float(input())
if d > max :
    max = d
if d < min :
    min = d
d = float(input())
if d > max :
    max = d
if d < min :
    min = d
d = float(input())
if d > max :
    max = d
if d < min :
    min = d
d = float(input())
if d > max :
    max = d
if d < min :
    min = d
print(min, max)

# 02_V3 (Adv: loop)
mn = float('inf')
mx = float('-inf')
for i in range(0, 6) :
    x = float(input())
    mn = min(mn, x)
    mx = max(mx, x)
print(mn, mx)

# 02_V3 (Adv: list comprehension + min & max functions)
ls = [float(input()) for _ in range(6)]
print(min(ls), max(ls))

# 02_V4 (Adv: list + loop)
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = int(input())
m = int(input())
y = int(input()) - 543
for i in range(m-1) :
    d += day[i]
# Leap year check
if m > 1 and (y % 400 == 0 or (y % 4 == 0 and y % 100 > 0)) :
    d += 1
print(d)