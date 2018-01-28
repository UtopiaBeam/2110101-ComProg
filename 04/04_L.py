# 04_L1 (Bug?)
print('ddbca'[int(input())-1])

# 04_L2
s = input().lower()
mx = 1
cnt = 1
nw = s[0]
for c in s[1:] :
    cnt = cnt+1 if nw == c else 1
    nw = nw if nw == c else c
    mx = max(mx, cnt)
print(mx)

# 04_L3 (Adv: sorted() + replace() + generator)
a, b = input(), input()
c, d = [sorted(s.lower().replace(' ', '')) for s in (a, b)]
print(a, b if c != d else '')