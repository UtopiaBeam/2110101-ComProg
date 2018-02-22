# 04_V1
print('bdccb'[int(input())-1])

# 04_V2
str = input()
ans = ''
for c in str :
    if c in "\"\',.()" :
        ans += ' '
    else :
        ans += c
print(ans)

# 04_V3
st, wd = input().strip().lower(), input().strip().lower()
s = ''
for c in st :
    if c not in '\'\",.' :
        s += c
print('Found' if ' ' + wd + ' ' in ' ' + s + ' ' else 'Not Found')

# 04_V3 (Adv: list)
st = ''.join([c for c in list(input().strip().lower()) if c not in '\'\",.'])
wd = input().strip().lower()
for c in st :
    if c not in '\'\",.' :
        str += c
ls = str.split()
print('Found' if wd in ls else 'Not Found')

# 04_V4 (Adv: list)
str = input().strip()
num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for i in range(len(str)) :
    if str[i].isdigit() :
        print(num[int(str[i])], end = '')
        if i < len(str) - 1 and (str[i+1].isdigit() or str[i+1].isalpha()) :
            print(end = ' ')
    else :
        print(str[i], end = '')