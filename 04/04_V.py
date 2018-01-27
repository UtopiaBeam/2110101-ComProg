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
st = input().lower()
wd = input().lower()
str = ''
for c in st :
    if c not in '\'\",.' :
        str += c
ls = str.split()
print('Found' if wd in ls else 'Not Found')

# 04_V4
str = input()
num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for i in range(int(len(str))) :
    if str[i] in '0123456789' :
        print(num[int(str[i])], end = '')
        if i < int(len(str)) - 1 and str[i+1] in '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM' :
            print(end = ' ')
    else :
        print(str[i], end = '')