# Sample_Q3_02
n, m, p = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(m)]
for i in range(n):
    for j in range(p):
        print(sum(a[i][k]*b[k][j] for k in range(m)), end = ' ')
    print()

# Sample_Q3_3
from collections import defaultdict as dict
n, usr, pgs = int(input()), dict(set), dict(set)
for _ in range(n) :
    inp = input().strip().split()
    for pg in inp[1:] :
        usr.setdefault(inp[0], set()).add(pg)
        pgs.setdefault(pg, set()).add(inp[0])
while True :
    inp = input().strip().split()
    if inp[0] == 'exit' :       break
    if inp[0] == 'common' :
        if inp[1] == 'page' :
            print(len(set.intersection(*[usr[x] for x in inp[2:]])))
        else :
            print(len(set.intersection(*[pgs[x] for x in inp[2:]])))
    else :
        if inp[1] == 'page' :
            print(min([x for x in pgs if x != inp[2]], key = lambda x : \
                (-len(pgs[x] & pgs[inp[2]])/len(pgs[x] | pgs[inp[2]]), x)))
        else :
            print(min([x for x in usr if x != inp[2]], key = lambda x : \
                (-len(usr[x] & usr[inp[2]])/len(usr[x] | usr[inp[2]]), x)))

# Sample_Q3_4
dc, odr, chk = dict(), dict(), []
cnt = 0
while True :
    nm, *ls = input().strip().split()
    if nm == 'end' :        break
    if nm not in odr :      odr[nm] = cnt
    cnt += 1
    for x in ls :
        if x not in dc.get(nm, []) :
            dc.setdefault(nm, []).append(x)
for _ in range(len(dc)) :
    mn = min(dc.keys(), key = lambda x : (sum(1 for t in dc[x] if t not in chk), odr[x]))
    ans = [t for t in dc[mn] if t not in chk][0]
    print(mn, ans)
    chk.append(ans)
    dc.pop(mn)
