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