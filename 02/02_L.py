# 02_L1
print('edcbe'[int(input()) - 1].lower())

# 02_L2 (Adv: sorted() + list comprehension)
print(sorted([int(input()) for _ in range(5)])[2])

# 02_L3
n = int(input())
if n < 0 or n > 80 :
    print("Error : Out of range")
else:
    out = ""
    out = str(n % 3) + out
    n //= 3
    out = str(n % 3) + out
    n //= 3
    out = str(n % 3) + out
    n //= 3
    out = str(n % 3) + out
    n //= 3
    print(out) 

# 02_L3 (Adv: loop)
n = int(input())
if n < 0 or n > 80 :
    print("Error : Out of range")
else :
    ans = ''
    for _ in range(0, 4) :
        ans = str(n%3) + ans
        n //= 3
    print(ans)

# 02_L4 (Adv: function)
from math import ceil
def e(nm) :
    w = [20, 100, 250, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]
    c = [32, 37, 42, 52, 67, 82, 97, 122, 137, 157, 177, 197, 217, 242, 267, 292, 317, 342, 367, 397, 427, 457, 487]
    return next((cs for cs, ws in zip(c, w) if nm <= ws), 'ERROR')
def r(nm) :
    w = [18, 22, 28, 38, 58]
    c = [100, 250, 500, 1000, 2000]
    return next((cs for cs, ws in zip(c, w) if nm <= ws), 'ERROR')
def n(nm) :
    return 5 + 15 * ceil(nm / 1000)
op = input().strip()
cs = int(input())
print( {'N' : n, 'E' : e, 'R' : r}[op](cs) if cs > 0 else 'ERROR' )



