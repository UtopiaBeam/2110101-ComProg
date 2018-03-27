# 09_P1
def function1():
    sum = 0
    for i in range(10):
        sum += i
    return sum
def function2(n):
    i = 2
    if n == 1:
        return False
    while i <= n**0.5:
        if n%i == 0:
            return False
        i += 1
    return True
def function3(n):
    for i in range(1,n):
        if function2(i):
            print(i)
def function4(x,y):
    match = 0  
    notmatch = ''
    for i in x:
        if i == y:
            match += 1
        else:
            notmatch += i
    return [match,notmatch]

f = input().strip()
if f == 'function1' :   print(function1())
if f == 'function2' :   print(function2(int(input())))
if f == 'function3' :   function3(int(input()))
if f == 'function4' :   print(function4(*input().strip().split()))

# 09_P2
from math import ceil
def nextEven(x) :
    x = ceil(x)
    return (x + 1) if x % 2 else x
def nextOdd(x) :
    x = ceil(x)
    return x if x % 2 else (x + 1)
while True :
    x = float(input())
    if x < 0 :      break
    print((nextEven(x), nextOdd(x)))

# 09_P3
def compare(a, b):
    return a[1] < b[1] or (a[1] == b[1] and a[0] > b[0])
n = int(input().strip())
d = []
for i in range(n):
    x, y = input().strip().split()
    d.append((x, float(y)))
for k in range(n-1):
    for i in range(n-1):
        if compare(d[i], d[i+1]):
            d[i], d[i+1] = d[i+1], d[i]
for i in d:
    print(i[0], i[1])

# 09_P4
def det3(m):
    a = m[0][0]*m[1][1]*m[2][2]
    b = m[0][1]*m[1][2]*m[2][0]
    c = m[0][2]*m[1][0]*m[2][1]
    d = m[0][2]*m[1][1]*m[2][0]
    e = m[0][0]*m[1][2]*m[2][1]
    f = m[0][1]*m[1][0]*m[2][2]
    return a+b+c-d-e-f
def det4(m):
    ans = 0
    for i in range(4) :
        ans += (-1)**(i) * m[0][i] *det3([[r[j] for j in range(4) if i != j] for r in m[1:]])
    return ans
matrix = []
for i in range(4):
    matrix.append([int(e) for e in input().split()])
print(det4(matrix))

# 09_P5
def roman_to_int(string):
    table = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C',100], ['XC',90],
             ['L', 50], ['XL', 40], ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]
    returnint=0
    for pair in table:
        check = True
        while check:
            if len(string) >= len(pair[0]):
                if string[0:len(pair[0])] == pair[0]:
                    returnint += pair[1]
                    string = string[len(pair[0]):]
                else:   check = False
            else:   check = False
    return returnint

print(*sorted([input().strip() for _ in range(int(input()))], key = roman_to_int), sep = '\n')

# 09_P6
def read_data():
    docs = {}
    n = int(input().strip())
    for i in range(n):
        tokens = input().strip().split()
        doc_name = tokens[0]
        doc_keywords = tokens[1:]
        for kword in doc_keywords:
            if kword in docs.keys():
                docs[kword].add(doc_name)
            else:
                docs[kword] = {doc_name}
    return docs
def search(docs, condition, search_keywords):
    if condition not in ['and', 'or'] :
        return set()
    ans = 0
    for word in search_keywords :
        if type(ans) == int :
            ans = (set() if word not in docs else docs[word])
        elif condition == 'and' :
            ans = ans & (set() if word not in docs else docs[word])
        else :      ans = ans | (set() if word not in docs else docs[word])
    return ans
docs = read_data()
tokens = input().split()
print( sorted( search(docs, tokens[0], tokens[1:]) ) )

# 09_P7 (Simplify the function)
def f(x) :      return x**2 + 2*x + 3
def f_inv(x) :  return int((x-2)**0.5) - 1 
print(eval(input().strip()))

# 09_P8 (zip())
def isSet(c1, c2, c3):
    return all(len(set([x, y, z])) in [1, 3] for x, y, z in zip(c1, c2, c3))
cards = []
for i in range(12):
    cards.append(input().strip().split())
for i in range(12):
    for j in range(i+1, 12):
        for k in range(j+1, 12):
            if isSet(cards[i], cards[j], cards[k]):
                print(i, j, k)

# 09_P9
def isSevenUp(x):
    return x % 7 == 0 or '7' in str(x)
def nextSevenUp(x):
    while not isSevenUp(x+1) :
        x += 1
    return x+1
def prevSevenUp(x):
    while not isSevenUp(x-1) :
        x -= 1
    return x-1

f, x = input().strip().split()
x = int(x)
if f == 'isSevenUp': print(isSevenUp(x))
elif f == 'nextSevenUp': print(nextSevenUp(x))
elif f == 'prevSevenUp': print(prevSevenUp(x))

# 09_P10 (zip())
def distance(p, q):
    return ( (p[0]-q[0])**2 + (p[1]-q[1])**2 )**0.5
def perimeter(points):
    return sum(distance(x, y) for x, y in zip(points, points[1:] + points[0:1]))
s = input().strip().split()
p = [(float(t[1:t.find(',')]), float(t[t.find(',')+1:-1])) for t in s]
print(perimeter(p))

# 09_P11
def zscore(L):
    mean = sum(L) / len(L)
    sd = (1/len(L) * sum( (x-mean)**2 for x in L))**0.5
    return [(x-mean)/sd for x in L]
L = [float(e) for e in input().split()]
for i in zscore(L):
    print(i)

# 09_P12
def eat(q1, q2):
    return any(q1[i] == q2[i] for i in range(2)) or abs(q1[0]-q2[0]) == abs(q1[1]-q2[1])
def all_eat(L):
    ls = []
    for i in range(len(L)) :
        for j in range(i+1, len(L)) :
            if eat(L[i], L[j]) :
                ls.append( (i, j) )
    return ls
print(eval(input().strip()))

# 09_P13
def row_number(t, e) :
    return [r for r in range(len(t)) if e in t[r]][0]
def flatten(t) :
    return [x for ts in t for x in ts if x != 0]
def inversions(t) :
    cnt = 0
    for i in range(len(t)) :
        for j in range(i+1, len(t)) :
            cnt += (t[i] > t[j])
    return cnt
def solvable(t) :
    inv = inversions(flatten(t))
    if len(t) % 2 :     return inv % 2 == 0
    return (inv + row_number(t, 0)) % 2 == 1

exec(input().strip())