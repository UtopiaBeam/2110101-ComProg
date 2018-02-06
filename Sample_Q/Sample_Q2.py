# Sample_Q2_1
t, cnt = int(input()), 0
for _ in range(t) :
    n, sum, ls = int(input()), 0, ''
    for i in range(1, n//2 + 1) :
        if n % i == 0 :
            sum += i
            ls += str(i) + ','
    print(str(n) + ' is' + (' not' if sum != n else '') + ' perfect')
    if sum == n :
        cnt += 1
        print(ls)
print(cnt)

# Sample_Q2_1 (Adv: list + map())
t, cnt = int(input()), 0
for _ in range(t) :
    n = int(input())
    ls = [x for x in range(1, n//2 + 1) if n % x == 0]
    print(n, 'is', 'perfect' if sum(ls) == n else 'not perfect')
    if sum(ls) == n :   print(','.join(map(str, ls)) + ',');   cnt += 1
print(cnt)

# Sample_Q2_2
b, s, e, m = int(input()), *input().strip().split()
s10, e10, m10 = [0] * 3
for c in s :    s10 = b*s10 + int(c)
for c in e :    e10 = b*e10 + int(c)
for c in m :    m10 = b*m10 + int(c)
for x in range(s10, e10, m10) :
    ans, t = '', x
    while t > 0 :
        ans = str(t % b) + ans
        t //= b
    print(ans or '0')

# Sample_Q2_2 (Adv: function + reduce())
def f(n, fr, to = 10) :
    ans, n = '', int(__import__('functools').reduce(lambda x, y : fr*int(x) + int(y), list(n)))
    while n > 0 :
        ans = str(n % to) + ans
        n //= to
    return int(ans or 0)
b, s, e, st = int(input()), *input().strip().split()
print(*(str(f(str(x), 10, b)) for x in range(f(s, b), f(e, b), f(st, b))), sep = '\n')

# Sample_Q2_3
fl, n, s = open('cards.txt'), int(input()), ''
for _ in range(n) :     s = fl.readline().strip()
pr, ans = 0, ''
for c in s :
    if c == 'A' :       nw = 1
    elif c == '0' :     nw = 10
    elif c == 'J' :     nw = 11
    elif c == 'Q' :     nw = 12
    elif c == 'K' :     nw = 13
    else :              nw = int(c)
    if pr > nw :        ans = 'N'
    pr = nw
print(ans or 'Y')

# Sample_Q2_3 (Adv: map + list + dict + sorted())
dc = { 'A' : 1, '0' : 10, 'J' : 11, 'Q' : 12, 'K' : 13 }
ls = [dc[x] if x in dc else int(x) for x in list(map(str.strip, open('cards.txt')))[int(input())-1]]
print('Y' if sorted(ls) == ls else 'N')

# Sample_Q2_4
ans, s = '', input().strip()
for i in range(len(s)) :
    for j in range(i, len(s)+1) :
        if s[i:j+1] == s[i:j+1][::-1] and (len(s[i:j+1]) > len(ans) or (len(s[i:j+1]) == len(ans) and ans > s[i:j+1])) :
            ans = s[i:j+1]
print(ans)