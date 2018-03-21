# 08_P1
ids, cts, odr = dict(), dict(), dict()
for i in range(int(input())) :
    x, ls = input().strip().replace(' ', '').split(':')
    if x not in ids :   ids[x] = []
    ids[x].extend(ls.split(','))
    odr[x] = i
    for c in ls.split(',') :
        if c not in cts :   cts[c] = []
        cts[c].append(x)
s = input().strip()
print(*sorted({x for c in ids[s] for x in cts[c] if x != s}, key = lambda x : odr[x]) or ['Not Found'], sep = '\n')

# 08_P1 (Adv: defaultdict)
from collections import defaultdict as dict
ids, cts, odr = dict(list), dict(list), dict(int)
for i in range(int(input())) :
    x, ls = input().strip().replace(' ', '').split(':')
    ids[x].extend(ls.split(','))
    odr[x] = i
    for c in ls.split(',') :
        cts[c].append(x)
s = input().strip()
print(*sorted({x for c in ids[s] for x in cts[c] if x != s}, key = lambda x : odr[x]) or ['Not Found'], sep = '\n')

# 08_P2
dc = dict()
for _ in range(int(input())) :
    nm, *ls = input().strip().split(', ')
    for x in ls :
        if x not in dc :    dc[x] = []
        dc[x].append(nm)
ls = input().strip().split(', ')
for x in ls :   print(x, '->', ', '.join(['Not found'] if x not in dc else dc[x]))

# 08_P2 (Adv: defaultdict)
from collections import defaultdict as dict
dc = dict(list)
for _ in range(int(input())) :
    nm, *ls = input().strip().split(', ')
    for x in ls :       dc[x].append(nm)
ls = input().strip().split(', ')
for x in ls :   print(x, '->', ', '.join(dc[x]) or 'Not found')

# 08_P3
dc, ls = dict(), list(map(int, input().strip().split()))
for x in ls :
    if x not in dc :    dc[x] = 0
    dc[x] += 1
print(min([x for x in ls if dc[x] == 1] or ['NONE']))

# 08_P3 (Adv: defaultdict)
dc, ls = __import__('collections').defaultdict(int), list(map(int, input().strip().split()))
for x in ls :
    dc[x] += 1
print(min([x for x in ls if dc[x] == 1] or ['NONE']))

# 08_P4
ls, n = list(map(int, input().split())), int(input())
print(sum(ls.count(n-x)-1 if n-x == x else ls.count(n-x) for x in ls) // 2)

# 08_P4 & P5 (1: Adv: defaultdict)
ls, n = list(map(int, input().split())), int(input())
dc = __import__('collections').defaultdict(int)
for x in ls :   dc[x] += 1
print(sum(dc[x]*dc[n-x] if x != n-x else dc[x]*(dc[x]-1) for x in ls) // 2)

# 08_P4 & P5 (2: Adv: Counter)
dc, n = __import__('collections').Counter(list(map(int, input().split()))), int(input())
print(sum(dc[x]*dc[n-x] if x != n-x else dc[x]*(dc[x]-1) for x in dc) // 2)

# 08_P6
n, m = map(int, input().split())
ls = list(map(int, input().split()))
dc, ans = {}, [False]*m

for i, x in enumerate(map(int, input().split())) :
    for j in range(n) :
        if x-ls[j] not in dc :  dc[x-ls[j]] = []
        dc[x-ls[j]].append((j, i))

for i in range(n) :
    for j in range(i+1, n) :
        sm = ls[i] + ls[j]
        if sm not in dc :   continue
        for k, idx in dc[sm] :
            if i != k and j != k :
                ans[idx] = True
print(*['YES' if flag else 'NO' for flag in ans], sep = '\n')            

# 08_P7 (Adv: defaultdict + lambda)
ls = [input().strip().split()[-1] for _ in range(int(input()))]
dc = __import__('collections').defaultdict(list)
for s in ls :
    dc[s[:2]].append(s)
ans = min(dc.keys(), key = lambda x : (-len(dc[x]), x))
print(ans, len(dc[ans]), *dc[ans], sep = '\n')

# 08_P8
a, b = (input().strip().split() for _ in range(2))
dc = dict([*zip(a, b), *zip(b, a)])
print(*[dc.get(x, x) for x in input().strip().split()])

# 08_P9 (Adv: defaultdict)
dc = __import__('collections').Counter([int(input()) for _ in range(int(input()))])
print(max(dc.keys(), key = lambda x : (dc[x], -x)))

# 08_P10
ls = [input().strip().split() for _ in range(int(input()))]
qr = input().strip().split()
ls = [l for l in ls if all(x in l[1:] for x in qr)]
print(*[' '.join(l) for l in sorted(ls)] or ['Not Found'], sep = '\n')

# 08_P11 (Adv: defaultdict + lambda)
ls = [set(input().strip().split()) for _ in range(int(input()))]
wd = input().strip()
ls = [l for l in ls if wd in l]
if not ls :     print('Not Found')
else :
    dc = __import__('collections').defaultdict(int)
    for l in ls :
        for ac in l :
            if ac != wd :   dc[ac] += 1
    if not dc :     print('No suggested event')
    else :
        ans = min(dc, key = lambda x : (-dc[x], x))
        print(ans, dc[ans], sep = '\n')

# 08_P12 (Adv: defaultdict + lambda)
ls = [set(input().strip().split()) for _ in range(int(input()))]
wd = input().strip()
ls = [l for l in ls if wd in l]
if not ls :     print('Not Found')
else :
    dc = __import__('collections').defaultdict(int)
    for l in ls :
        for ac in l :
            if ac != wd :   dc[ac] += 1
    if not dc :     print('No suggested event')
    else :
        for tp in sorted(zip(dc.keys(), dc.values()), key = lambda tp : (-tp[1], tp[0])) :
            print(*tp)

# 08_P13 (Adv: defaultdict)
ls = [ln.strip().split() for ln in __import__('sys').stdin]
ls, wd = ls[:-1], *ls[-1]
dc = __import__('collections').defaultdict(list)
for tp in ls :
    dc[tp[0]].append(tp[1])
    dc[tp[1]].append(tp[0])
ans = {wd} | set(dc[wd]) | set(val for key in dc[wd] for val in dc[key])
print(*sorted(ans), sep = '\n')

# 08_P14
dc = dict(input().strip().split() for _ in range(int(input())))
ls = sorted([input().strip().split() for _ in range(int(input()))], key = lambda l : -float(l[1]))
ans = []
for l in ls :
    for dp in l[2:] :
        if dp not in dc :   continue
        if type(dc[dp]) != 'int' :
            dc[dp] = int(dc[dp])
        if dc[dp] > 0 :
            ans.append((l[0], dp))
            dc[dp] -= 1
            break
print(*[' '.join(tp) for tp in sorted(ans)], sep = '\n')

# 08_P15
cr, nm = (dict(tuple(ln.strip().split(',')) for ln in open(input().strip())) for _ in range(2))
for ln in open(input().strip()) :
    x, y = ln.strip().split(',')
    print('record error' if x not in cr or y not in nm else cr[x] + ',' + nm[y])

# 08_P16
ls = [set(input().strip().split()) for _ in range(int(input()))]
print(len(set.union(*ls or [set()])), len(set.intersection(*ls or [set()])), sep = '\n')

# 08_P17
dc, ls = dict(), [input().strip().split() for _ in range(int(input()))]
for _, l in ls :
    dc[l] = False
print(sorted(set(w for w, _ in ls if w not in dc or dc[w])), sep = '\n')