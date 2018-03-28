# 10_L1
print('CE AB H J DHJMN'.split()[int(input()) - 1])

# 10_L2
def x(n) :
    if n == 0 :     return 0.01
    tmp = x(n-1)
    return 3*tmp*(1-tmp)
def M(n) :
    return 1 if n <= 1 else M(n-1) + sum(M(k)*M(n-2-k) for k in range(n-1))
def D(m, n) :
    return 1 if m*n == 0 else D(m-1, n) + D(m-1, n-1) + D(m, n-1)
def S(n) :
    return 1 if n < 3 else 1/n * ((6*n-9)*S(n-1) - (n-3)*S(n-2))
def d(n) :
    return 1 if n < 1 else n*d(n-1) + (-1)**n

exec(input().strip())

# 10_L3
def dhanoi(n, left, mid, right):
    if n == 0 :     return
    dhanoi(n-1, left, mid, right)
    print(str(n)+'W', ':', left, '->', mid)
    print(str(n)+'B', ':', left, '->', mid)
    dhanoi(n-1, right, mid, left)
    print(str(n)+'B', ':', mid, '->', right)
    print(str(n)+'W', ':', mid, '->', right)
    dhanoi(n-1, left, mid, right)
exec(input().strip())

# 10_L4
def copylist(x):
    return [copylist(e) if type(e) == list else e for e in x]
exec(input().strip())