# 59_3_Q3_2_p
d0, d1 = list(map(int, input().split())), list(map(int, input().split()))
out = []
if input().strip() == 'z':
    while d0 and d1:
        out += [d0[0], d1[0]]
        d0, d1 = d0[1:], d1[1:]
    out += d0 + d1
else:
    while d0 and d1:
        if d0[0] < d1[0]:
            out.append(d0[0])
            d0 = d0[1:]
        else:
            out.append(d1[0])
            d1 = d1[1:]
    out += d0 + d1
print(out)

# 59_3_Q3_3_p
n = int(input())
ls = [input().split() for _ in range(n)]
op = input().strip()
if op == 'show':
    print(*[' '.join(l) for l in ls], sep='\n')
else:
    dc = dict((l[0], list(map(float, l[1:]))) for l in ls)
    op, t = op.split()
    if op == 'get':     print(t, *dc.get(t, ['not found']))
    if op == 'avg':     print(round(sum(l[int(t)-1] for l in dc.values())/n, 4))
    if op == 'max':
        mx = min(dc, key=lambda x: (-dc[x][int(t)-1], x))
        print(mx, dc[mx][int(t)-1])
    if op == 'sort':    print(*sorted(dc, key=lambda x: (dc[x][int(t)-1], x) ))

# 59_3_Q3_4_p
ls, q = list(), list()
nw, nx, tm = 0, 0, 0
for _ in range(int(input())):
    op = input().strip()
    if op == 'next':
        print('call', ls[0][0])
        nx, tm = ls.pop(0)
    elif op == 'avg_qtime':
        print('avg_qtime', round(sum(q)/len(q), 4))
    else:
        op, t = op.split()
        t = int(t)
        if op == 'reset':       nw = t
        if op == 'new':
            ls.append( (nw, t) )
            print('ticket', nw)
            nw += 1
        if op == 'order':
            dt = t-tm
            q.append(dt)
            print('qtime', nx, dt)
        