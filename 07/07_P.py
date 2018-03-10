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
n = int(input())
ls = [-int(input()) for _ in range(n)]
print(*[-x for x in sorted(ls)], sep = '\n')