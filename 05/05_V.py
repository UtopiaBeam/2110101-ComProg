# 05_V1
print('abedd'[int(input())-1])

# 05_V2
n = int(input())
fl = open('data.txt', 'r')
for l in fl :
    if 'Name' in l :
        n -= 1
    if n == 0 :
        print(l[6:])
        break
if n > 0 :      print('Not Found')
fl.close()

# 05_V2 (Adv: map())
fl = list(map(str.strip, open('data.txt', 'r')))
n, ls = int(input()), [s[6:] for s in fl[::4]]
print('Not Found' if n > len(ls) else ls[n-1])

# 05_V3
filename = input().strip()
found_id = ''
f = open(filename, 'r')
for line in f :
    if line[:10] not in found_id :
        found_id += line[:10] + ';'
print(*found_id.split(';'), sep = '\n')
f.close()

# 05_V3 (Adv: repeat + OrderedDict)
from itertools import repeat
from collections import OrderedDict
fl = map(lambda s : s[:10], open(input().strip()))
print(*OrderedDict(zip(fl, repeat(None))).keys(), sep = '\n')

# 05_V4 (Adv: Counter() + sorted() + map())
from collections import Counter
cnt = Counter(''.join(open(input().strip())))
s = ''.join(map(str.strip, (input().strip() for _ in range(3))))
print(*sorted(s, key = lambda c : cnt.get(c, 0))[::-1], sep = '')