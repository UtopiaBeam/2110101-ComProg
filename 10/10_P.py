# 10_P1
def fac(n) :
    return 1 if n < 2 else n*fac(n-1)
print(fac(int(input())))

# 10_P2
def fb(n) :
    return n if n < 2 else fb(n-1)+fb(n-2)
print(fb(int(input())))

# 10_P3
def C(n, k) :
    return 1 if k in [0, n] else (0 if n == 0 else C(n-1, k-1) + C(n-1, k))
print(C(int(input()), int(input())))

# 10_P4
def pm(a, k, m) :
    x = pm(a, k//2, m) if k > 0 else 1
    return [x*x, x*x*a][k%2] % m
print(pm(*map(int, input().split())))

# 10_P5
def isinlist(ls, x) :
    return any(e == x if type(e) != list else isinlist(e, x) for e in ls)
print('Found' if isinlist(eval(input().strip()), int(input().strip())) else 'Not Found')

# 10_P6
def ks(i, w, v, x) :
    if i < 0 :      return 0
    if x >= w[i] :  return max(ks(i-1, w, v, x), ks(i-1, w, v, x-w[i]) + v[i])
    return ks(i-1, w, v, x)
w, v = (list(map(int, input().split())) for _ in range(2))
W = int(input())
print(ks(len(w)-1, w, v, W))

# 10_P7
def f(d, c, s, b, m) :
    if s == len(d)-1 :      return m+1
    if b :      return f(d, c+1, s+1, True, max(c+1, m)) if d[s+1] >= d[s] else f(d, 0, s+1, False, m)
    return f(d, 1, s+1, True, m) if d[s+1] >= d[s] else f(d, 0, s+1, False, m)
d = [int(e) for e in input().split()]
print(f(d, 0, 0, False, 0))

# 10_P8
def gcd(x, y) :
    return gcd(y, x%y) if y else x
print(gcd(*map(int, input().split())))

# 10_P9
def isSorted(L):
    if len(L) <= 2 :    return True
    if L[0] <= L[1] <= L[-1] :      return isSorted(L[1:])
    if L[0] >= L[1] >= L[-1]:       return isSorted(L[1:])
    return False

n = int(input())
L = [int(e) for e in input().split()]
if isSorted(L):     print('true')
else:       print('false')

# 10_P10
def tiling(n, c) :
    return 1 if n == 1 else 2*tiling(n-1, 'B') + (tiling(n-1, 'G') if c != 'G' else 0)
N = int(input())
print(tiling(N, 'G') + tiling(N, 'R') + tiling(N, 'B'))

# 10_P11
def same_row(i, j) :     return (i//9 == j//9)
def same_col(i, j) :     return (i-j) % 9 == 0
def same_block(i, j) :   return (i//27 == j//27 and i%9//3 == j%9//3)
def show(board) :
    for i in range(3) :
        print('+---+---+---+')
        for j in range(3) :
            k = 9*(3*i+j)
            print('|' + board[k:k+3] + '|' + board[k+3:k+6] + '|' + board[k+6:k+9] + '|')
    print('+---+---+---+')
def solve(board) :
    idx = board.find('.')
    if idx < 0 :        return board
    T = set('123456789') - set(board[i] for i in range(len(board)) \
        if same_block(idx, i) or same_row(idx, i) or same_col(idx, i))
    for e in T :
        newboard = board[:idx] + e + board[idx+1:]
        sol = solve(newboard)
        if sol :        return sol
    return ''
sol = solve(input().strip())
show(sol)

# 10_P12
def doublelist(ls) :
    return [x if type(x) != list else doublelist(x) for x in ls for _ in range(2)]
print(doublelist(eval(input().strip())))

# 10_P13 (Backtracking)
ans = set()
def gen(s, i=0, wd=[]) :
    if i == len(s) :
        ans.add(''.join(wd))
        return
    if s[i].isupper() :     gen(s, i+1, wd)
    wd.append(s[i])
    gen(s, i+1, wd)
    wd.pop()
gen(input().strip())
print(*sorted(ans), sep = '\n')

# 10_P14
def dfs(nw, e) :
    if nw == e :    return True
    return any(dfs(nx, e) for nx in dc.get(nw, []))

n, s, e = map(int, input().split())
dc = dict()
for _ in range(n) :
    x, y = map(int, input().split())
    dc.setdefault(x, []).append(y)
print(['no', 'yes'][dfs(s, e)])

# 10_P15 (Backtracking)
ans = []
def dfs(nw, e, ls=[]) :
    ls.append(nw)
    if nw == e :
        ans.append(' -> '.join(map(str, ls)))
    else : 
        for nx in sorted(dc.get(nw, set())) :
            dfs(nx, e)
    ls.pop()

n, s, e = map(int, input().split())
dc = dict()
for _ in range(n) :
    x, y = map(int, input().split())
    dc.setdefault(x, set()).add(y)
dfs(s, e)
print(*ans or ['no'], sep = '\n')

# 10_P16
def B_to_A(ls) :
    if len(ls) == 1 :       return [ls]
    ans = []
    for x in ls[::-1] :
        if type(x) == list :
            ans = B_to_A(x) + ans
        else :      ans = [[x]+l for l in ans]
    return ans
print(B_to_A(eval(input().strip())))

# 10_P17
def flatten_dict(dc) :
    ans = dict()
    for x, y in dc.items() :
        if type(y) == dict :
            for k, v in flatten_dict(y).items() :
                ans[x+'.'+k] = v
        else :      ans[x] = y
    return ans
a = eval(input())
fa = flatten_dict(a)
for k in sorted(fa.keys()):
    print(k, ':', fa[k])

# 10_P18
def dfs(board ,level ,ans,max_depth) :
    if board == (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0) :
        print(ans)
        return True
    if level == max_depth or board == "" :
        return False
    if dfs(up(board),level+1,ans+"U",max_depth) :
        return True
    if dfs(down(board),level+1,ans+"D",max_depth) :
        return True
    if dfs(left(board),level+1,ans+"L",max_depth) :
        return True
    if dfs(right(board),level+1,ans+"R",max_depth) :
        return True
def up(board) :
    loc = board.index(0)
    if loc//4 == 0 :    return ""
    board = list(board)
    board[loc], board[loc-4] = board[loc-4], board[loc]
    return tuple(board)
def down(board) :
    loc = board.index(0)
    if loc//4 == 3 :    return ""
    board = list(board)
    board[loc], board[loc+4] = board[loc+4], board[loc]
    return tuple(board)
def left(board) :
    loc = board.index(0)
    if loc%4 == 0 :    return ""
    board = list(board)
    board[loc], board[loc-1] = board[loc-1], board[loc]
    return tuple(board)
def right(board) :
    loc = board.index(0)
    if loc%4 == 3 :    return ""
    board = list(board)
    board[loc], board[loc+1] = board[loc+1], board[loc]
    return tuple(board)
    
board = tuple(map(int, input().split()))
found = False
for max_depth in range(1,10):
    if dfs(board,0,"",max_depth):
        found = True
        break
if not found:   print("Cannot find answer")