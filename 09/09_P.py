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