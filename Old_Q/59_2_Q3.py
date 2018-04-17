# 59_2_Q3_2_p
ls, n = [int(x) for x in input().split()], int(input())
if n < min(ls):       print('Too short')
elif n > max(ls):    print('Too tall')
else:   print((len(ls)-sorted(ls+[n])[::-1].index(n))*100/len(ls), 'th percentile', sep = '')

# 59_2_Q3_3_p
def print_money(s, m) :
    sorted_m = sorted([ (v, m[v]) for v in m ])
    sorted_m = sorted_m[::-1]
    print(s,','.join([str(v)+":"+str(c) for v,c in sorted_m if c>0]))
money = input().strip().split(",")
pocket_money = dict()
for item in money :
    v, c = [int(e) for e in item.split(":")]
    pocket_money[v] = c
print_money("In pocket:", pocket_money)
pocket_amount = sum(x*y for x, y in pocket_money.items())
pay_amount = int(input())
if pay_amount > pocket_amount :
    print("Not enough money")
else :
    pay_money = dict()
    sorted_money = sorted([ (v, pocket_money[v]) for v in pocket_money ])
    sorted_money = sorted_money[::-1]
    p = pay_amount
    for value,count in sorted_money :
        if value*count > p:
            c = p // value
        else :
            c = count
        p -= value*c
        pay_money[value] = c
    if p != 0 :
        print("Not match")
    else :
        print_money("Pay:", pay_money)
        for x, y in pay_money.items() :
            pocket_money[x] -= y
        print_money("Left in pocket:", pocket_money)

# 59_2_Q3_4_p
dc, n = {}, int(input())
for _ in range(n):
    ln = input().strip().split(',')
    dc.setdefault(ln[1], set()).add(ln[0])
print(*sorted(dc, key = lambda x: (-len(dc[x]), x))[:3], sep = ',')