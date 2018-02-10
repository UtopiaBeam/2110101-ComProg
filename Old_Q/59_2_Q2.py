# 59_2_Q2_2_p (Adv: list)
n, neg, ls = input().strip(), False, []
print(n, '=', end = ' ')
if n == '0' :       print('0')
else :
    if n[0] == '-' :
        print('-', end = '')
        neg = True
        n = n[1:]
    while n :
        if n[0] != '0' :    ls.append('{}*{}'.format(n[0], 10**(len(n)-1)))
        n = n[1:]
print((' - ' if neg else ' + ').join(ls))

# 59_2_Q2_3_p
s, ans = input().strip(), ''
while s :
    if not s[0].isdigit() :
        ans, s = ans + s[0], s[1:]
        continue
    p, n = int(s[0]), int(s[1])
    l, s = s[2:2+n], s[2+n:]
    for c in l :
        if '0' <= c <= '9'   :    ans += chr((ord(c)-ord('0')+p) % 10 + ord('0'))
        elif 'a' <= c <= 'z' :    ans += chr((ord(c)-ord('a')+p) % 26 + ord('a'))
        elif 'A' <= c <= 'Z' :    ans += chr((ord(c)-ord('A')+p) % 26 + ord('A'))
        else :      ans += c
print(ans)

# 59_2_Q2_4_p
fl, n, ls = open(input().strip()), int(input()), []
for ln in fl :
    ls.append(ln.strip().split(';', 1)[1])
    if ';Failure' in ls[-1] :
        print(*ls[-n-1:], sep = '\n')
        break
else :      print('Not Found')
