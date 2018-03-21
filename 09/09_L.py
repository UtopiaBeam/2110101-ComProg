# 09_L1
print('daaea'[int(input())-1])

# 09_L2
def knows(R, x, y) :
    return y in R[x]
def is_celeb(R, x) :
    return len([y for y in R[x] if x != y]) == 0 and all(x in R[y] for y in R if x != y)
def find_celeb(R) :
    ans = None
    for x in R :
        if is_celeb(R, x) :
            ans = x
    return ans
def read_relations() :
    R = dict()
    while True:
        d = input().strip().split()
        if len(d) == 1 :    break
        if d[0] not in R :  R[d[0]] = set()
        if d[1] not in R :  R[d[1]] = set()
        R[d[0]].add(d[1])
    return R
def main() :
    R = read_relations()
    c = find_celeb(R)
    if c == None :  print('Not Found')
    else :      print(c)
exec(input().strip())