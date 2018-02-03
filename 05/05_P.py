# 05_P1 (Adv: next() + generator + map() + lambda + zip())
grd = lambda x : next((gr for sc, gr in zip([50, 55, 60, 65, 70, 75, 80], ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+']) if sc > x), 'A')
for ls in map(str.split, open(input().strip())) :
   print(ls[0], grd(sum(map(int, ls[1:]))))

# 05_P2 (Adv: next() + generator + map() + lambda + zip())
grd = lambda x : next((gr for sc, gr in zip([50, 55, 60, 65, 70, 75, 80], ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+']) if sc > x), 'A')
it = iter(open(input().strip()))
for _ in range(int(next(it))) :
    ls = next(it).split()
    print(ls[0], grd(sum(map(int, ls[1:]))))

# 05_P3 (Adv: dict + map() + get())
print(dict(map(str.split, open('score.txt'))).get(input().strip(), 'Not Found'))

# 05_P4 (Adv: dict + sum())
dc, cnt = { 'BE' : 0, 'SE' : 1, 'VE' : 2, 'ET' : 3 }, [0] * 4
for l in open(input().strip()) :
    t = l.split()[0].upper()
    if t in dc :    cnt[dc[t]] += 1
print(*cnt, sum(cnt))

# 05_P5 (Adv: map())
print(*(j in i for i, j in zip(map(str.strip, open(input().strip())), map(str.strip, open(input().strip())))), sep = '\n')

# 05_P6 (Adv: map() + sum())
f1, f2 = (list(map(str.strip, open(input().strip()))) for _ in range(2))
for n in f1 :
    print(sum(map(float, f2[:int(n)])) / float(n))
    f2 = f2[int(n):]

# 05_P7
cnt = 0
for l in open(input().strip()) :
    if l.strip() == '' :
        cnt += 1
print(cnt)

# 05_P8 (Adv: dict + function)
op, wd, *ls = (l.strip() for l in open(input().strip()))
fn = {'find' : lambda s, l = 0, r = -1 : s.find(wd, l, r),
      'rfind' : lambda s, l = 0, r = -1 : s.rfind(wd, l, r)}[op]
for ln in ls :
    s, l, r = ln.split()
    it = fn(s, int(l), int(r))
    print(s[max(0, it-1) : min(len(s), it+len(wd)+1)] if it >= 0 else 'not found')

# 05_P7 (Adv: sum())
print(sum(1 for l in open(input().strip()) if not l.strip()))