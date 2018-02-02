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