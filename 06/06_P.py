# 06_P1
ls = []
while True :
    ls.append(int(input()))
    if ls[-1] < 0 :     break
for x in ls[:-1] :
    print(x + ls[-1])

# 06_P1 (Adv: sys.stdin)
ls = [int(x) for x in __import__('sys').stdin]
print(*[x+ls[-1] for x in ls[:-1]], sep = '\n')

# 06_P2
ls, [s, e] = [int(input()) for _ in range(int(input()))], list(map(int, input().split()))
print(sum(ls[s:e+1]))

# 06_P3
n, ls = int(input()), list(map(float, input().split()))
print(sum(ls) / len(ls))

# 06_P4
ls = list(map(float, input().split()))[:-1]
print(sum(ls) / len(ls))

# 06_P5 (Adv : sys.stdin)
print(*(w*10000/h**2 for w, h in [map(int, s.strip().split()) for s in __import__('sys').stdin if len(s.strip().split()) > 1]), sep = '\n')

# 06_P5
while True :
    ls = list(map(int, input().strip().split()))
    if ls[0] == -1 :    break
    print(ls[0]*10000 / ls[1]**2)

# 06_P6
ls = list(map(int, input().split()))
print(*(sum(ls[max(0, i-1) : min(len(ls), i+2)]) // (min(len(ls), i+2)-max(0, i-1)) for i in range(len(ls))))

# 06_P7
a, b = (map(int, input().strip()[1:-1].split(',')) for _ in range(2))
print(sum([x*y for x, y in zip(a, b)]))

# 06_P8
ls = list(range(1, int(input())+1))
while True :
    x, y = map(int, input().split())
    if x == y == 0 :    break
    x, y = map(ls.index, [x, y])
    ls[x], ls[y] = ls[y], ls[x]
print(ls)

# 06_P9
ls = input().strip().split()
print(*(ls[int(i)] for i in input().strip().split()))

# 06_P10
ls = [int(x) for x in input().split(', ')] + [0]
print(sum(1 for x, y in zip(ls, ls[1:]) if x < 0 and y >= 0))

# 06_P11
ls = list(map(int, input().split()))
ls = [ls.pop(0 if ls[0] > ls[-1] else -1) for _ in range(len(ls))]
x, y = sum(ls[::2]), sum(ls[1::2])
print(x, y, [x == y, x > y, x < y].index(True), sep = '\n')

# 06_P12
s, n = list(input().strip()), int(input())
for _ in range(n) :
    op, *ls = input().strip().split()
    if op == 'in' :     s.insert(int(ls[1]), ls[0])
    if op == 'out' :    s.pop(int(ls[0]))
    if op == 'swap' :   s[int(ls[0])], s[int(ls[1])] = s[int(ls[1])], s[int(ls[0])]
    print(''.join(s))

# 06_P13
dc, nw = {i+1 : int(input()) for i in range(int(input()))}, -1
while nw != 1 :
    print(abs(nw), end = ' ')
    nw = dc[abs(nw)]

# 06_P14
ls = []
while True :
    inp = input().strip().split(' ', 1)
    if inp[0] == 'return' :
        ls.append(inp[1])
        print(len(ls))
    elif inp[0] == 'shelf' :    print('no book' if not ls else ls.pop())
    elif inp[0] == 'top' :      print('no book' if not ls else ls[-1])
    elif inp[0] == 'list' :     print(ls)
    else :      break
