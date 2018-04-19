# 59_3_Q4_2_p
def p(n):
    if 0 <= n <= 2:     return 1
    if n >= 3:      return p(n-2) + p(n-3)
def m(n):
    if n <= 2:      return 1
    tmp = m(n-2)
    return m(tmp) + m(n-tmp)
def e(n):
    if n in [2, 3]:     return 1
    if n > 3:       return sum(e(k+1)*e(n-k) for k in range(1, n-1))
def s(n, k):
    if n == 0:      return 2
    tmp = s(n-1, k)
    return (tmp**2 - tmp + 1) % k
exec(input().strip())

# 59_3_Q4_3_p
def read_data():
    D = dict()
    n = int(input())
    for k in range(n):
        sid,name,gpax,year,dept = [e.strip() for e in input().strip().split(',')]
        gpax = float(gpax); year = int(year)
        if dept not in D :
            D[dept] = {sid:(name,gpax,year)}
        else :
            D[dept][sid] = (name,gpax,year)
    return D
def is_in(D, sid, dept):
    return sid in D.get(dept, [])
def get_year(D, sid):
    res = False
    for dc in D.values():
        res = dc.get(sid, (None, None, False))[-1] or res
    return res
def get_supers(D, dept):
    if dept not in D:   return False
    return {sid for sid, tp in D[dept].items() if tp[-1] > 4}
def max_gpax(D):
    return max(gpa for dc in D.values() for _, gpa, __ in dc.values())
def get_max_gpax_students(D):
    mx = max_gpax(D)
    return {(sid, name) for dc in D.values() for sid, (name, gpa, _) in dc.items() if gpa == mx}
n = int(input())
for k in range(n):
    exec(input().strip())

# 59_3_Q4_4_p
like, liked = dict(), dict()
while True:
    inp = input().strip()
    if inp == 'done':       break
    inp = inp.split()
    like.setdefault(inp[0], []).extend(inp[1:])
    for c in inp[1:]:   liked.setdefault(c, []).append(inp[0])
inp = input().strip().split()
if inp[0] == 'R':
    print(*sorted('{} {}'.format(key, len(ls)) for key, ls in like.items()), sep='\n')
elif inp[0] == 'T':
    mx = max(len(ls) for ls in liked.values())
    print(*sorted(key for key, ls in liked.items() if len(ls) == mx), sep='\n')
elif inp[0] == 'C':
    print(*sorted(set(liked.get(inp[1], [])) & set(liked.get(inp[2], []))) or ['None'], sep='\n')
else:
    print(*sorted((x, y) for x in like for y in like.get(x, []) if x in like.get(y, [])) or ['None'], sep='\n')