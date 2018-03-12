# 07_P1
cnt = [0]*10
for x in input().strip() :
    cnt[int(x)] += 1
print(*cnt, sep = '\n')

# 07_P2
cnt = [0]*62
for x in input().strip() :
    if x.isdigit() :    cnt[int(x)] += 1
    elif x.isupper() :  cnt[ord(x)-ord('A')+10] += 1
    else :      cnt[ord(x)-ord('a')+36] += 1
print(*cnt)

# 07_P3
ls = []
for ln in open('score.txt') :
    ls.append(list(map(int, ln.strip().split())))
while True :
    n = int(input())
    if n < 0 :      break
    for l in ls :
        if n == l[0] :
            print(l[1])
            break
    else :      print('Not Found')

# 07_P3 (Adv: dict)
dc = {}
for ln in open('score.txt') :
    dc.setdefault(*ln.strip().split())
while True :
    n = input().strip()
    if n == '-1' :      break
    print(dc[n] if n in dc else 'Not Found')

# 07_P4
ls = []
while True :
    ls.append(int(input()))
    if ls[-1] == -1 :
        ls = ls[:-1]
        break
ls.sort()
cnt, mx, num = 1, 1, ls[0]
for i in range(1, len(ls)) :
    if ls[i] == ls[i-1] :
        cnt += 1
    else :      cnt = 1
    if mx < cnt :
        mx, num = cnt, ls[i]
print(num if mx > len(ls)//2 else 'Not found')

# 07_P5
ls = [-int(input()) for _ in range(int(input()))]
print(*[-x for x in sorted(ls)], sep = '\n')

# 07_P5 (Adv: lambda)
print(*sorted([int(input()) for _ in range(int(input()))], key = lambda x : -x), sep = '\n')

# 07_P6
n = int(input())
ls = sorted([float(input()) for _ in range(n)])
avg, mean = sum(ls)/n, (ls[(n-1)//2]+ls[n//2])/2
mode, cnt, mx = ls[0], 1, 1
for i in range(1, len(ls)) :
    cnt = [1, cnt+1][ls[i] == ls[i-1]]
    if cnt > mx :       mx, mode = cnt, ls[i]
print(avg, mean, mode)

# 07_P6 (Adv: lambda)
n = int(input())
ls = sorted([float(input()) for _ in range(n)])
print(sum(ls)/n, (ls[(n-1)//2]+ls[n//2])/2, max(ls, key=ls.count))

# 07_P7
print(*sorted([ln.strip().split()[0] for ln in open('score.txt')]), sep = '\n')

# 07_P8
print(*sorted([ln.strip().split()[0] for ln in open('score.txt')])[::-1], sep = '\n')

# 07_P9
ls = list(map(int, input().split()))
print(*sorted([x for x in ls if not x%2]), *sorted([x for x in ls if x%2])[::-1])

# 07_P10
n = int(input())
ls = [input().strip() for _ in range(n)]
cnt = 0
for i in range(n) :
    for j in range(n-1) :
        if len(ls[j]) > len(ls[j+1]) or len(ls[j]) == len(ls[j+1]) and ls[j] > ls[j+1] :
            ls[j], ls[j+1] = ls[j+1], ls[j]
            cnt += 1
print(*ls, cnt, sep = '\n')

# 07_P11
n, _ = map(int, input().split())
for _ in range(n) :
    ls, avg = [c for c in input().strip().split() if c != 'X'], 0
    for c in ls :
        if c == 'A'    :    avg += 4
        elif c == 'B+' :    avg += 3.5
        elif c == 'B'  :    avg += 3
        elif c == 'C+' :    avg += 2.5
        elif c == 'C'  :    avg += 2
        elif c == 'D+' :    avg += 1.5
        elif c == 'D'  :    avg += 1
    print('%.2f' % (avg/len(ls)))

# 07_P11 (Adv: dict + zip())
n, _ = map(int, input().split())
dc = dict(zip('A B+ B C+ C D+ D F'.split(), [4, 3.5, 3, 2.5, 2, 1.5, 1, 0]))
for _ in range(n) :
    ls = [dc[c] for c in input().strip().split() if c != 'X']
    print('%.2f' % (sum(ls)/len(ls)))

# 07_P12 (1)
op, n = map(int, input().split())
ls = [[int(x) for x in input().split()] for _ in range(n)]
ans = 0
for i in range(n) :
    for j in range(n) :
        if (op == 0 and i >= j) or (op == 1 and i <= j) :
            ans += ls[i][j]
print(ans)

# 07_P12 (2)
op, n = map(int, input().split())
ls = [[int(x) for x in input().split()] for _ in range(n)]
print(sum([ls[i][j] for i in range(n) for j in range(n) if [i>=j, i<=j][op]]))

# 07_P13
r, c = int(input()), int(input())
ls = [input().strip() for _ in range(r)]
for i in range(r) :
    for j in range(i+1, r) :
        if ls[i] == ls[j] :
            print(i+1, ls[i], j+1, ls[j], sep = '\n')

# 07_P14
r, c = map(int, input().split())
ls = [[int(c) for c in input().split()] for _ in range(r)]
flag = True
for i in range(r) :
    for j in range(c) :
        mn_r, mx_c = min(ls[i]), 0
        for k in range(r) :
            mx_c = max(mx_c, ls[k][j])
        if mn_r == mx_c == ls[i][j] :
            print(ls[i][j])
            flag = False
if flag :   print(-1)

# 07_P14 (Adv: zip())
r, c = map(int, input().split())
ls = [[int(c) for c in input().split()] for _ in range(r)]
ans = [ls[i][j] for i in range(r) for j in range(c) if ls[i][j] == min(ls[i]) == max(list(zip(*ls))[j])]
print(-1 if not ans else ans[0])

# 07_P15 (1)
n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
for i in range(n) :
    cnt_r = cnt_c = 0
    for j in range(n) :
        cnt_r += ls[i][j]
        cnt_c += ls[j][i]
    if cnt_r == 1 and cnt_c == n :
        print(i)
        break
else :      print(-1)

# 07_P15 (2: all())
n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
for i in range(n) :
    if ls[i].count(1) == 1 and all(ls[j][i] == 1 for j in range(n)) :
        print(i)
        break
else :      print(-1)

# 07_P16
r, c = map(int, input().split())
a, b = [[list(map(int, input().split())) for _ in range(r)] for _ in range(2)]
print(*[' '.join([str(a[i][j]+b[i][j]) for j in range(c)]) for i in range(r)], sep = '\n')

# 07_P17
ls, x = [], None
while True :
    x = input().strip().split()
    if len(x) == 1 :    break
    ls.append(x)
ls = [l[0] for l in sorted(ls, key = lambda x : [-float(x[-1]), int(x[0])])]
print('Not Found' if x[0] not in ls else ls.index(x[0])+1)

# 07_P18 (string.ascii_lowercase)
ls = [input().strip() for _ in range(int(input()))]
print(*sorted(ls, key = lambda s : [s.count(c) for c in __import__('string').ascii_lowercase] + [s]), sep = '\n')