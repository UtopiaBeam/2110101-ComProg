# 06_V1
print(['x', 'k', 'tu', 'c', 'h'][int(input())-1])

# 06_V2 (Adv: zip + next())
ans = []
for ls in [l.strip().split(';') for l in open(input().strip())] :
    grd = next(gr for gr, sc in zip('ABCDF', [80, 70, 60, 50, 0]) if sum(map(float, ls[3:])) >= sc)
    ans.append([ls[0], '{} {}'.format(*ls[1:3]), grd])
print(ans)

# 06_V3 (Adv: zip + next())
ans = []
for ls in [l.strip().split(';') for l in open(input().strip()) if l.strip()] :
    grd = next(gr for gr, sc in zip('ABCDF', [80, 70, 60, 50, 0]) if sum(map(float, ls[3:])) >= sc)
    ans.append([ls[0], '{} {}'.format(*ls[1:3]), grd])
while True :
    n = input().strip()
    if n == '-1' :      break
    print(next((x for x in ans if n in x), 'Not Found'))

# 06_V4 (Adv: dict + lambda)
dc, od = {}, {}
for k, v in [l.strip().split() for l in open(input().strip())] :
    dc.setdefault(k, []).append(v)
    if k not in od :    od[k] = len(od)
print(sorted([[k, dc[k]] for k in dc], key = lambda x : od[x[0]]))
print('The most favorite fruit is', max(dc.items(), key = lambda x : len(x[1]))[0])