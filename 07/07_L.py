# 07_L1
print(['j', 'k', 'g', 'tu', 'n'][int(input())-1])

# 07_L2 (1 : Selectoin Sort)
ls = list(map(int, input().split()))
for i in range(len(ls)-1) :
    mn_idx = i+1
    for j in range(i, len(ls)) :
        if ls[mn_idx] > ls[j] :
            mn_idx = j
    ls[i], ls[mn_idx] = ls[mn_idx], ls[i]
print(ls)

# 07_L2 (2 : sorted())
print(sorted([int(x) for x in input().split()]))

# 07_L3
ls = sorted([float(x) for x in input().split()])
print(ls[len(ls)//2] if len(ls) % 2 > 0 else (ls[len(ls)//2-1] + ls[len(ls)//2]) / 2)

# 07_L4
ls = []
for ln in open('inventory.txt') :
    code, name, amount = ln.strip().split(';')
    ls.append([code, name, int(amount)])
while True :
    inp = input().strip().split()
    if inp[0] == 'T' :
        for i in range(len(ls)) :
            if ls[i][0] == inp[1] :
                ls[i][2] += int(inp[2])
                print(ls[i])
                break
        else :      print('Product code does not exist.')
    elif inp[0] == 'U' :
        for i in range(len(ls)) :
            if ls[i][0] == inp[1] :
                ls[i][2] = int(inp[2])
                print(ls[i])
                break
        else :      print('Product code does not exist.')
    elif inp[0] == 'A' :
        flag = True
        inp[3] = int(inp[3])
        for i in range(len(ls)) :
            if ls[i][0] == inp[1] :
                print('Duplicate product code.')
                flag = False
                break
        if flag :
            print(inp[1:])
            ls.append(inp[1:])
    elif inp[0] == 'D' :
        flag = True
        for i in range(len(ls)) :
            if ls[i][0] == inp[1] :
                ls[i:i+1] = []
                print(inp[1], 'deleted')
                flag = False
                break
        if flag :       print('Product code does not exist.')
    else :
        print('Bye!')
        break