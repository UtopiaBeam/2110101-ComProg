# 10_V1
print('chmcgqahkceg'[int(input())-1])

# 10_V2
def h(n) :
    return 2*h(n-1)+1 if n > 0 else 0
def gcd(x, y) :
    return gcd(y, x%y) if y > 0 else x
def J(n, k) :
    return (J(n-1, k)+k) % n if n > 0 else 0
def C(n) :
    return sum(C(k)*C(n-1-k) for k in range(n)) if n > 0 else 1
def f(n):
    if n <= 1 :     return n 
    return f((n+1)//2)**2 + f(n//2)**2 if n % 2 == 1 else (2 * f(n//2-1) + f(n//2)) * f(n//2)
def F(n) :
    return n - M(F(n-1)) if n > 0 else 1
def M(n) :
    return n - F(M(n-1)) if n > 0 else 0
def A(m, n) :
    if m == 0 :     return n+1
    return A(m-1, 1) if n == 0 else A(m-1, A(m, n-1))

exec(input().strip())

# 10_V3
import random
def qsort(d) :
    if len(d) <= 1 :    return d
    p = d[random.randint(0, len(d)-1)]
    le = [x for x in d if x < p]
    eq = [x for x in d if x == p]
    mo = [x for x in d if x > p]
    return qsort(le) + eq + qsort(mo)

d = [int(e) for e in input().split()]
d = qsort(d)
print(' '.join([str(e) for e in d]))

# 10_V4
def sumlist(x):
    return sum(e if type(e) == int else sumlist(e) for e in x)
print(sumlist(eval(input().strip()))) 