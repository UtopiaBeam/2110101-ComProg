# 05_L1
print('dcddd'[int(input())-1])

# 05_L2 (Adv: defaultDict)
from collections import defaultdict as dict
dc, cnt, ls = dict(int), dict(int), list(map(lambda s : tuple(s.strip().split(':')[2:]), open('data.txt', 'r')))
for sec, scr in ls :
    dc[int(sec)] += float(scr)
    cnt[int(sec)] += 1
n = int(input().strip())
print(dc[n]/cnt[n] if n in dc else 'Not Found')

# 05_L3
f = open(input().strip())
c_sum = 0
for l in f :
    for c in l:
        c_sum = c_sum ^ ord(c)
f.close()
print(c_sum)

# 05_L3 (Adv: reduce() + __xor__)
print(__import__('functools').reduce(int.__xor__, map(ord, ''.join(open(input().strip())))))

# 05_L4
f = ''.join(open(input().strip(), 'r'))
n, w, r = int(input().strip()), input().strip('\n\r'), input().strip('\n\r')
i = 0
for _ in range(n) :
    while i < len(f) :
        if f[i:i+len(w)].lower() == w.lower() :
            f = f[:i] + r + f[i+len(w):]
            break
        else :      i += 1
    i += 1
print(f)