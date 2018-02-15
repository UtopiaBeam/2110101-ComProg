# 04_P1
s = input().strip()
sum = 0
for x in s :
    if x.isupper() :
        sum += 1
print(sum)

# 04_P1 (Adv: sum() + generator)
print(sum(1 for x in input().strip() if x.isupper()))

# 04_P2
s = input().strip()
c, v = 0, 0
for x in s :
    if x.isalpha() :
        if x.lower() in 'aeiou' :
            v += 1
        else :
            c += 1
print(v, c)

# 04_P2 (Adv: reduce())
from functools import reduce
print(*reduce(lambda v, c : (v[0] + c[0], v[1] + c[1]),
        ((1, 0) if x.lower() in 'aeiou' else (0, 1) for x in input().strip() if x.isalpha())))

# 04_P3
a, b = input().split()
sum = 0
for x in b :
    if x.isdigit() :
        sum += int(x)
print(a[0].upper() + a[1:].lower(), sum)

# 04_P3 (Adv: title() + sum())
a, b = input().split()
print(a.title(), sum(int(x) for x in b if x.isdigit()))

# 04_P4 (Adv: map())
m, d, y = map(int, input().strip().split('/'))
print(format(d, '02d'), ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'][m-1]  , y)

# 04_P5 & P6
s = input().strip()
print(s + str(sum(1 for x in s if x == '1') % 2))

# 04_P5 & P6 (Adv: map())
s = input().strip()
print(s + str(sum(map(int, s)) % 2))

# 04_P7
s = input().strip()
ans = [x for x in range(10) if str(x) not in s]
if ans :    print(*ans)
else :      print('No missing digits')

# 04_P7 (Adv: set() + sorted())
st = set('0123456789') - set(input().strip())
if st :     print(*sorted(st))
else :      print('No missing digits')

# 04_P8
a = input().lower()
chk = True
for i in range(1, len(a)) :
    if a[i-1] > a[i] :
        chk = False
        break
print('yes' if chk else 'no')

# 04_P8 (Adv: list + sorted())
a = list(input().lower())
print('yes' if a == sorted(a) else 'no')

# 04_P9
str, a, b = (input().strip() for _ in range(3))
ans = ''
for c in str :
    if c == a :     ans += b
    elif c == b :   ans += a
    else :          ans += c
print(ans)

# 04_P9 (Adv: dict)
str, a, b = (input().strip() for _ in range(3))
print(*( {a : b, b : a}[c] if c in [a, b] else c for c in str ), sep = '')

# 04_P10
str, a, b = (input().strip() for _ in range(3))
ans = ''
for c in str :
    chk = True
    for i in range(len(a)) :
        if c == a[i] :      ans += b[i];    chk = False
        elif c == b[i] :    ans += a[i];    chk = False
    if chk :    ans += c
print(ans)

# 04_P10 (Adv: dict + zip())
str, a, b = (input().strip() for _ in range(3))
dc = dict([*zip(a, b), *zip(b, a)])
print(*(dc[c] if c in dc else c for c in str), sep = '')

# 04_P11
s = input().strip()
l, r = (int(x) for x in input().strip().split())
print(s[:l] + s[l:r+1][::-1] + s[r+1:])

# 04_P12
s = input().strip().lower().replace(' ', '')
print('yes' if s == s[::-1] else 'no')

# 04_P13
s = input().strip() + ' '
cnt = 0
for i in range(len(s)-1) :
    if s[i] in 'aeiou' and s[i+1] not in 'aeiou' :
        cnt += 1
print(cnt)

# 04_P13 (Adv: sum() + zip())
s = input().strip().lower()
idx = [i for i in range(len(s)) if s[i] in 'aeiou']
print(sum(1 for i, j in zip(idx, idx[1:]) if i+1 != j) + 1 if idx else 0)

# 04_P14
s = input().strip() + '+'
if s[0] not in '+-' :
    s = '+' + s
ans, num, op = 0, 0, 1
for x in s :
    if x in '+-' :
        ans += op * num
        num = 0
        if x == '+' :   op = 1
        else :          op = -1
    else :
        num = 10*num + int(x)
print(ans)

# 04_P14 (Adv: eval())
print(eval(input().strip()))

# 04_P15 (Adv: defaultDict)
from collections import defaultdict as dict
dc = dict(int)
ls = []
for c in input().strip() :
    dc[c] += 1
    ls.append((c, dc[c]))
print(*(c for c, x in ls if dc[c] == 1 or x == 2), sep = '')

# 04_P16 (Adv: list + function)
num = ['soon', 'nueng', 'song', 'sam', 'see', 'ha', 'hok', 'jed', 'pad', 'kao']
dig = ['', '', 'sip', 'roey', 'pun', 'muen', 'saen']
sp = [('nueng-sip', 'sip'), ('sip-nueng', 'sip-ed'), ('song-sip', 'yee-sip')]
n, d, *_ = tuple([*input().strip().replace(',', '').split('.'), ''])
ls = []
def th(n) :
    while len(n) > 0 :
        if n[0] in '123456789' :
            ls.append(num[int(n[0])])
            if len(n) > 1 :     ls.append(dig[len(n)])
        n = n[1:]
if '-' in n :
    print('lop-', end = '')
    n = n[1:]
if n == '0' :
    ls.append('soon')
    n = n[1:]
while len(n) > 6 :
    th(n[:-6])
    n = n[-6:]
    ls.append('larn')
th(n)
if d :      ls.append('jood')
for x in d :
    ls.append(num[int(x)])
ans = '-'.join(ls)
for x, y in sp :
    ans = ans.replace(x, y)
print(ans)

# 04_P17 (Adv: reduce() + zip() + dict + function)
from functools import reduce
num = dict(zip(['soon', 'nueng', 'song', 'sam', 'see', 'ha', 'hok', 'jed', 'pad', 'kao'], range(10)))
dig = dict(zip(['sip', 'roey', 'pun', 'muen', 'saen'], [10**x for x in range(1, 7)]))
sp = [('yee-sip', 'song-sip'), ('sip-ed', 'sip-nueng')]
n, d, *_ = (*input().strip().split('-jood-'), '')
n = reduce(lambda a, b : a.replace(*b), sp, n).split('-')
ans, tmp, neg = 0, 0, False
for c in n :
    if c == 'lop' :     neg = True
    elif c in num :     tmp += num[c]
    elif c == 'larn' :
        ans, tmp = (ans+tmp) * 10**6, 0
    else :
        if c == 'sip' and tmp == 0 :
            tmp = 10
        else :
            ans += tmp * dig[c]
            tmp = 0
print(format(-ans-tmp if neg else ans+tmp, ',d'), end = '')
if d :  print('.', *[num[x] for x in d.split('-')], sep = '')

# 04_P18
n = int(input())
ls = [input().strip() for _ in range(n)]
pre = suf = ls[0]
for s in ls :
    tmp = ''
    for i in range(min(len(pre), len(s))) :
        if s[i] != pre[i] :     break
        tmp += s[i]
    pre, tmp = tmp, ''
    for i in range(-1, -1-min(len(suf), len(s)), -1) :
        if s[i] != suf[i] :     break
        tmp = s[i] + tmp
    suf, tmp = tmp, ''
print(pre or 'NO COMMON PREFIX')
print(suf or 'NO COMMON SUFFIX')

# 04_P18 (Adv: os.path.commonprefix())
from os.path import commonprefix
n = int(input())
ls = [input().strip() for _ in range(n)]
print(commonprefix(ls) or 'NO COMMON PREFIX')
ls = [s[::-1] for s in ls]
print(commonprefix(ls)[::-1] or 'NO COMMON SUFFIX')

# 04_P19
a, b = input().strip(), input().strip()
ans = []
for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' :
    if c in a and c in b :
        ans.append(c)
print(' '.join(ans) if ans else 'NONE')

# 04_P19 (Adv: set + sorted())
print(' '.join(sorted(set(input().strip()) & set(input().strip()), key = str.swapcase))  or 'NONE')

# 04_P20 (Adv: dict + function)
x, y = 0, 0
dc = {
    'U' : lambda x, y : (x, y+1),
    'D' : lambda x, y : (x, max(0, y-1)),
    'L' : lambda x, y : (max(0, x-1), y),
    'R' : lambda x, y : (x+1, y)
}
for c in input().strip() :
    x, y = dc[c](x, y)
print('({},{})'.format(x, y))

# 04_P21
a, b = input().strip(), input().strip()
if a in b :     print('SUBSTRING')
else :
    while a and b :
        if a[0] == b[0] :
            a = a[1:]
        b = b[1:]
    print('NONE' if a else 'SUBSEQUENCE')

# 04_P21 (Adv: iter())
a, b = input().strip(), input().strip()
ia, ib = iter(a), iter(b)
print(['NONE', 'SUBSEQUENCE', 'SUBSTRING'][(a in b) + all(any(ca == cb for cb in ib) for ca in ia)])
