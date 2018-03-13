# 08_L1
print('dbacd'[int(input())-1])

# 08_L2
ls = [(tuple(ln.strip().split()[:-1]), ln.strip().split()[-1]) for ln in open('address.txt')]
addr, tel = dict(ls), dict([(y, ' '.join(x)) for x, y in ls])
while True :
    s = input().strip()
    if not s :      break
    if s.isdigit() :    print(tel.get(s, 'Not Found'))
    else :      print(addr.get(tuple(s.split()), 'Not Found'))

# 08_L3
file = open(input().strip())
count = dict()
t = 'abcdefghijklmnopqrstuvwxyz0123456789 '
for line in file :
    line_wo_symbols = ''
    for c in line.lower() :
        if c in t : line_wo_symbols += c
    for word in line_wo_symbols.split() :
        if word not in count.keys() :
            count[word] = -1
        else :
            count[word] -= 1
file.close()
wordcounts = [(count[word],word) for word in count.keys()]
sorted_wordcounts = sorted(wordcounts)
print([(tp[1], -tp[0]) for tp in sorted_wordcounts[:10]])

# 08_L4 (issubset())
wds = set(input().strip().split(', '))
flag = True
for ln in open('books.txt') :
    if wds.issubset(set(ln.strip().split(', ')[1:])) :
        print(ln.strip().split(', ')[0])
        flag = False
if flag :       print('Not found')