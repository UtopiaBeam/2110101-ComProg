# 03_L1
print(['a', 'o', 'n', 'p', 'egjv'][int(input())-1])

# 03_L2
x = int(input())
k = 0
ans = 0
while x > 0 :
    ans += (x % 10) * (2**k)
    k += 1
    x //= 10
print(ans)

# 03_L2 (Adv: list)
x = input()[::-1]
ans = 0
while len(x) > 0 :
    ans = 2 * ans + int(x[-1])
    x = x[:-1]
print(ans)

# 03_L3
x, b = [int(e) for e in input().split()]
if x < 0 or not 2 <= b <= 9 :
    print('Error: Cannot convert')
else :
    ans = ''
    while x > 0 :
        ans = str(x % b) + ans
        x //= b
    print(ans)

# 03_L4
n = int(input())
ans = 0
for i in range(1, n+1) :
    for j in range(1, i+1) :
        for k in range(1, j+1) :
            ans += ((-1)**i) * j * k
print(ans)