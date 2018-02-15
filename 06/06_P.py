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