# 07_V1
print('dadbe'[int(input())-1])

# 07_V2 (Bubble Sort)
x, op = [int(x) for x in input().split()], input().strip()
for i in range(len(x)-1) :
    for j in range(len(x)-1) :
        if (op == 'a' and x[j] > x[j+1]) or (op == 'd' and x[j] < x[j+1]) :
            x[j], x[j+1] = x[j+1], x[j]
print(x)

# 07_V2 (Adv: sorted() + function + dict)
x, op = [int(x) for x in input().split()], input().strip()
print(sorted(x, key = lambda a : [a, -a][op == 'd']))

# 07_V3
infile = open("hotels.txt", "r")
hotels = []
for line in infile :
    [hotel, stars, review] = line.strip().split(";")
    hotels.append([hotel, int(stars), float(review)])
infile.close()
star = int(input())
found_hotels = []
for h in hotels:
    if h[1] >= star :
        found_hotels.append(h)
if len(found_hotels) == 0 :
    print("Not Found")
else :
    for i in range(len(found_hotels)-1) :
        for j in range(len(found_hotels)-1) :
            if found_hotels[j][-1] < found_hotels[j+1][-1] :
                found_hotels[j], found_hotels[j+1] = found_hotels[j+1], found_hotels[j]
    for ls in found_hotels :
        print(*ls)
    
# 07_V3 (Adv: lambda)
n, ls = int(input()), []
for ln in open('hotels.txt') :
    if n <= int(ln.strip().split(';')[1]) :
        ls.append(ln.strip().split(';'))
if not ls :     print('Not Found')
else :
    for ln in sorted(ls, key = lambda x : -float(x[-1])) :
        print(*ln)

# 07_V4 (Adv: lambda)
n, ls = int(input()), []
for ln in open('circulations.txt') :
    if n > int(ln.strip().split()[-1]) :
        ls.append(ln.strip().split())
if not ls :     print('Not Found')
else :      print(*[' '.join(ln) for ln in sorted(ls, key = lambda x : int(x[-1]))], sep = '\n')