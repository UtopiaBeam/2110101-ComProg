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

# 09_L3
def extract_sign(t):
    sign = ''
    if t[0] == '-':
        t = t[1:]
        sign = 'lop-'
    return sign,t
def split_by_point(t):
    k = t.find('.')
    d = ''
    if k >= 0:
        d = t[k+1:]
        t = t[:k]
    return t, d
def remove_comma(t):
    return t.replace(',', '')
def split_by_million(t):
    tm = ''
    if len(t) > 6 :
        tm = t[:-6]
        t = t[-6:]
    return tm,t
def digit_to_text(d):
    digits = 'soon nuengsong sam  see  ha   hok  jed  pad  kao  '
    return digits[d*5:d*5+5].strip()
def pos_to_text(p):
    pos = '     siproey punmuensaenlarn'
    return pos[p*4:p*4+4].strip()
def right_of_jood_to_text(t):
    out = ''
    for d in t:
        out += '-' + digit_to_text(int(d))
    return out
def number_to_text(t):
    t1 = ''
    for p in range(len(t)):
        c = t[len(t)-p-1]
        if c == '0' :   continue
        tmp = digit_to_text(int(c)) + '-' + pos_to_text(p)
        if p == 0 :     t1 = tmp
        else:       t1 = tmp + '-' + t1
    t1 = t1[:-1]
    if t1[-5:] == '-soon' :     t1 = t1[:-5]
    t1 = t1.replace('song-sip', 'yee-sip')
    t1 = t1.replace('nueng-sip', 'sip')
    t1 = t1.replace('sip-nueng', 'sip-ed')
    return t1
def combine(moreM, lessM):
    if moreM.strip('soon'):
        if lessM.strip('soon') :  return (moreM + '-larn-' + lessM).strip('-')
        return moreM + '-larn'
    return lessM or 'soon'
def main():
    num = input().strip()
    sign, num = extract_sign(num)
    leftJ, rightJ = split_by_point(num)
    leftJ = remove_comma(leftJ)
    moreM, lessM = split_by_million(leftJ)
    tLessM = number_to_text(lessM)
    tMoreM = number_to_text(moreM)
    out = combine(tMoreM, tLessM)
    if rightJ != '' :
        out += '-jood'
        for d in rightJ:
            out += '-' + digit_to_text(int(d))

    print(sign + out)

exec(input().strip())

# 09_L4
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