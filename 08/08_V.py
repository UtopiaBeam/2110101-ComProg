# 08_V1
print('ceedc'[int(input())-1])

# 08_V2 (Adv: reduce())
s1, s2 = [set([s for ln in open(name) for s in __import__('functools').reduce(lambda x, y : \
    x.replace(y, ' '), '\'\"-.(),', ln.strip().lower()).split()]) for name in 'file1.txt file2.txt'.split()]
wd = input().lower().strip()
print(['Not found', 'Found in file1 only', 'Found in file2 only', 'Found in both files'][2*(wd in s2) + (wd in s1)])

# 08_V3
dc = dict([(tuple(ln.strip().split()[:2]), ln.strip().split()[2:]) for ln in open('address.txt')])
while True :
    s = tuple(input().strip().split())
    if not s :      break
    print(*dc.get(s, ['Not found']))

# 08_V4
dc = dict()
while True :
    ln = input().strip().split()
    if len(ln) == 1 :   break
    for c in ln[1:] :
        if c not in dc :    dc[c] = set()
        dc[c].add(ln[0])
s1, s2 = [dc.setdefault(c, set()) for c in input().strip().split()]
print(len(s1 & s2), len(s1 ^ s2), len(s1 | s2))

# 08_V4 (Adv: defaultdict)
from collections import defaultdict as dict
dc = dict(set)
while True :
    ln = input().strip().split()
    if len(ln) == 1 :   break
    for c in ln[1:] :
        dc[c].add(ln[0])
s1, s2 = [dc[c] for c in input().strip().split()]
print(len(s1 & s2), len(s1 ^ s2), len(s1 | s2))