# 59_3_Q2_2_p
op = input().strip()
if op == 'A' :
    m, p, q = (int(input().strip()) for _ in range(3))
    for i in range(m+1) :
        for j in range(p) :
            if i+j > q :
                print('P3', i, j)
                break
            if j == p-1 :   print('P4', i, j)
elif op == 'B' :
    m, p = (int(input().strip()) for _ in range(2))
    i = c = 0
    while i <= m :
        j = i
        while j <= p :
            print(i, j)
            c, j = c+1, j+1
        i += 1
    print(c)
else :      print('Invalid op')

# 59_3_Q2_3_p
s, op = (input().strip().upper() for _ in range(2))
for c in s :
    if c not in 'ACGT' :
        print('Invalid DNA')
        break
else :
    if op == 'R' :
        for c in s[::-1] :
            if c == 'A' :       print('T', end = '')
            if c == 'G' :       print('C', end = '')
            if c == 'C' :       print('G', end = '')
            if c == 'T' :       print('A', end = '')
    elif op == 'F' :
        a = g = c = t = 0
        for x in s :
            if x == 'A' :       a += 1
            if x == 'G' :       g += 1
            if x == 'C' :       c += 1
            if x == 'T' :       t += 1
        print('A={}, T={}, G={}, C={}'.format(a, t, g, c))
    else :
        p, cnt = input().strip(), 0
        for i in range(len(s)-len(p)) :
            if p == s[i:i+len(p)] :
                cnt += 1
        print(cnt)

# 59_3_Q2_3_p (Adv: dict + zip() + Counter)
s, op = (input().strip().upper() for _ in range(2))
for c in s :
    if c not in 'ACGT' :
        print('Invalid DNA')
        break
else :
    if op == 'R' :
        dc = dict(zip('ACGT', 'TGCA'))
        print(*(dc[c] for c in s[::-1]), sep = '')
    elif op == 'F' :
        cnt = dict(__import__('collections').Counter(s))
        print(', '.join('{}={}'.format(c, cnt.get(c, 0)) for c in 'ATGC'))
    else :
        ls = [s[i] + s[i+1] for i in range(len(s)-1)]
        print(ls.count(input().strip()))
    
# 59_3_Q2_4_p (Adv: set + map + zip)
op = input().strip()
ls = [input().strip() for _ in range(int(input().strip()))]
ln = len(ls[0])
if len(set(map(len, ls))) > 1 :
    print('Invalid size')
elif op == 'flip' :
    print(*[s[::-1] for s in ls], sep = '\n')
else :
    for _ in range(int(op) // 2) :
         ls = [''.join(tp) for tp in zip(*ls[::-1])]
    print(*ls, sep = '\n')
