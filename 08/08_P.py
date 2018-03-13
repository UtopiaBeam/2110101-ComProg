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

# 08_P2 (Adv: defaultdict)
from collections import defaultdict as dict
dc = dict(list)
for _ in range(int(input())) :
    nm, *ls = input().strip().split(', ')
    for x in ls :       dc[x].append(nm)
ls = input().strip().split(', ')
for x in ls :   print(x, '->', ', '.join(dc[x]) or 'Not found')

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