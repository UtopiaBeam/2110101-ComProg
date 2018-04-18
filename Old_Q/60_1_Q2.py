# 60_1_Q2_00_p
def list2dict(x):
    d = dict()
    for a, (b, c) in x:
        d.setdefault(c, []).append( (a, b) )
    return d
def dict2list(d):
    x = [[fr, (se, key)] for key, ls in d.items() for fr, se in ls]
    return x
def get_empty(d):
    ans = {x for x in d if not d[x]}
    return ans
def compress_string(s) :
    if not s:       return ()
    nw, cnt = '', 0
    ls = []
    for c in s:
        if c != nw:
            ls.append( (nw, cnt) )
            cnt = 0
        nw, cnt = c, cnt+1
    return tuple(ls[1:] + [ (nw, cnt) ])
def a(n) :
    if n <= 1:      return [3, 1][n]
    x, y = a(n-1), a(n-2)
    return [2*x+y+3, 3*x-2*y-n][n%2]
exec(input().strip())
exec(input().strip())

# 60_1_Q2_0a_p
def add(d1, d2):
    ans = dict(d1)
    for x, y in d2.items():
        ans[x] = y + ans.get(x, 0)
        if ans[x] == 0:     ans.pop(x)
    return ans
def common(x1, x2) :
    return sorted([x for x in x1 if x in x2])
def get_zero_positions(x) :
    ans = set()
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == 0:
                ans.add( (i, j) )
    return ans
def a(n) :
    if n <= 2:      return 2-n
    if n%3 == 0:    return 3*a(n-1)*a(n-2) - n**2
    return 2*a(n-3) + 1
exec(input().strip())

# 60_1_Q2_1_p
def next_boards(board):
    results = list()
    nw = list(board)
    idx = nw.index(0)
    r, c = idx//3, idx%3
    if r > 0:
        nw[idx], nw[idx-3] = nw[idx-3], nw[idx]
        results.append( (tuple(nw), 'U') )
        nw[idx], nw[idx-3] = nw[idx-3], nw[idx]
    if r < 2:
        nw[idx], nw[idx+3] = nw[idx+3], nw[idx]
        results.append( (tuple(nw), 'D') )
        nw[idx], nw[idx+3] = nw[idx+3], nw[idx]
    if c > 0:
        nw[idx], nw[idx-1] = nw[idx-1], nw[idx]
        results.append( (tuple(nw), 'L') )
        nw[idx], nw[idx-1] = nw[idx-1], nw[idx]
    if c < 2:
        nw[idx], nw[idx+1] = nw[idx+1], nw[idx]
        results.append( (tuple(nw), 'R') )
        nw[idx], nw[idx+1] = nw[idx+1], nw[idx]
    return sorted(results)

command = input().strip()
start_board = tuple([int(c) for c in list(input().strip())])
if command == '1':
    print(next_boards(start_board))
elif command == '2':
    pendings = [ (start_board , "") ]
    while len(pendings) > 0:
        (current_board , moves) = pendings.pop(0)
        if current_board == (1,2,3,4,5,6,7,8,0):
            print(moves)
            break
        results = next_boards(current_board)
        new_boards_and_moves = [(b,moves+direction) for (b,direction) in results]
        pendings.extend(new_boards_and_moves)

# 60_1_Q2_2a_p
def cmp(tp):
    s = tp[1]
    if s[2].isupper():      ch = [x for x in s[3:] if x.isupper()][0]
    else:       ch = [x for x in s[3:] if x.islower()][0]
    return (ch.lower(), ch)
n, op = input().strip().split()
ls = []
for _ in range(int(n)):
    ln = input().strip().split()
    if ln[1] == op:     ls.append( (ln[0], ln[2]) )
print(*[tp[0] for tp in sorted(ls, key = cmp)] or ['Not Found'], sep='\n')

# 60_1_Q2_3_p
def f(choices, n, conditions):
    if n == 0:      return [{}]
    return add_choice(choices, f(choices, n-1, conditions), conditions)
def add_choice(choices, solutions, conditions) :
    res = []
    for dc in solutions:
        for c in choices:
            if conditions.get(c, float('inf')) > dc.get(c, 0):
                tmp = dict(dc)
                if c not in tmp:    tmp[c] = 0
                tmp[c] += 1
                res.append(tmp)
    return res
def show(solutions):
    if len(solutions) == 0:     print([])
    else :
        ans = set()
        for soln in solutions :
            x = sorted([(k,v) for k,v in soln.items()])
            ans.add(tuple(x))
        print('\n'.join([str(list(soln)) for soln in sorted(ans)]))
exec(input().strip())
exec(input().strip())