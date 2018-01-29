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
        sum += ord(x) - ord('0')
print(a[0].upper() + a[1:].lower(), sum)

# 04_P3 (Adv: title() + sum())
a, b = input().split()
print(a.title(), sum(ord(x) - ord('0') for x in b if x.isdigit()))

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
s = input()
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
    if ord(a[i-1]) > ord(a[i]) :
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

# 04_P13 (Adv: enumerate() + sum() + zip())
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
        num = 10*num + ord(x) - ord('0')
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
