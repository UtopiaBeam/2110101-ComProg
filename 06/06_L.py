# 06_L1
print('cbbdc'[int(input())-1])

# 06_L2
ls = [int(x) % 2 for x in input().split()]
print(ls, sum(ls), sep = '\n')

# 06_L3
ls = list(map(int, input().split()))
print(ls[len(ls)%2::2][-1] + ls[len(ls)%2::2][1] - ls[len(ls)%2::2][0])

# 06_L4
s = list(map(int, input().split()))
n, ls = len(s) // 2 + 1, [s]
for i in range(n-1) :
    ls.append(list(map(int, input().split())))
ls, ans = ls[::-1], 0
for i in range(len(ls)) :
    ans += sum(ls[i][i:len(s)-i])
print(ans)

# 06_L4 (Adv: sys.stdin)
ls = [list(map(int, s.split())) for s in __import__('sys').stdin][::-1]
print(sum(sum(x[i:len(x)-i]) for i, x in enumerate(ls)))