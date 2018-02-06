# 59_2_Q1_2_p (Adv: list)
d, m, y = (int(x) for x in input().split())
d, y = d+15, y-543
if m == 2 :     n = 29 if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0) else 28
else :          n = 31 if m in [1, 3, 5, 7, 8, 10, 12] else 30
if d > n :      d, m = d-n, m+1
if m > 12 :     m, y = m-12, y+1
print(d, m, y+543, sep = '/')