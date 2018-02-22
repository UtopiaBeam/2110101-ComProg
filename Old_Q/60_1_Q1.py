# 60_1_Q1_2a_p
from math import sqrt
c = input().strip()
if c not in 'RSP' :     print('Invalid')
elif c == 'S' :
    m = int(input().strip())
    q, r, t, k, n, x, i, p = 1, 0, 1, 1, 3, 3, 0, ''
    while i < m :
        if 4*q + r - t < n*t :
            p += str(n)
            a = 10 * (r - n*t)
            n = 10 * (3*q + r) // t - 10*n
            q *= 10
            r = a
            i += 1
        else :
            a = (2*q + r) * x
            b = (7*q*k + 2 + x*r) // (x*t)
            q *= k
            t *= x
            x += 2
            k += 1
            n, r = b, a
    print('pi =', p[0] + '.' + p[1:])
elif c == 'R' :
    p = 0
    for k in range(int(input().strip()) + 1) :
        p += (-3)**(-k) / (2*k + 1)
    p = round(sqrt(12)*p, 12)
    print('pi =', p)
else :      print('pi =', round(sqrt(7 + sqrt(6 + sqrt(5))), 6))

# 60_1_Q1_3a_p (Adv: tuple + dict)
fl = open(input().strip())
op, ls = fl.readline().strip(), [tuple(s.split(']')) for s in fl.readline().strip().split('[') if s]
if op == 'M2T' :
    for ln in fl :
        try :       print(''.join([dict(ls)[x] for x in ln.strip().split()]))
        except :    print('Invalid :', ln.strip())
elif op == 'T2M' :
    for ln in fl :
        try :       print(' '.join([dict([(j, i) for i, j in ls])[x] for x in ln.strip()]))
        except :    print('Invalid :', ln.strip())
else :      print('Invalid code')

# 60_1_Q1_4a_p
ls, n = ['10' if c == 'X' else c for c in input().strip()], int(input())
fr, sc, nw = [], [0]*12, 0
for i in range(9) :
    t = 1 if ls[nw] == '10' else 2
    fr.extend([i+1] * t)
    nw += t
fr.extend([10] * (len(ls)-nw))
ls = [10-int(ls[i-1]) if c == '/' else int(c) for i, c in enumerate(ls)] + [0, 0]
for i in range(len(ls) - 2) :
    sc[fr[i]] += ls[i]
    if fr[i] == 10 :        continue
    if ls[i] == 10 :        sc[fr[i]] += ls[i+1] + ls[i+2]
    elif ls[i] + ls[i-1] == 10 and fr[i] == fr[i-1]:
        sc[fr[i]] += ls[i+1]
print(sc[n] if 1 <= n <= 10 else sum(sc))