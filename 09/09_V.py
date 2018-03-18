# 09_V1
print('adjapegeeb'[int(input())-1])

# 09_V2
def fac(n) :
    return str(n) + '!'

def oneterm(x, n) :
    return str(x) + '**' + str(n) + '/' + fac(n)

def sin(x, n) :
    out, k, sign = str(x), 3, '-'
    for i in range(n-1) :
        out += ' ' + sign + ' ' + oneterm(x, k)
        k += 2
        sign = ['-', '+'][sign == '-']
    return out

exec(input().strip())

# 09_V3
mname = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,
 "May":5,"Jun":6,"Jul":7,"Aug":8,
 "Sep":9,"Oct":10,"Nov":11,"Dec":12} 

def read_date() :
    d, m, y = input().strip().split()
    return (int(d), mname[m], int(y))

def zodiac(d, m) :
    if d >= 22 and m==3 or d <=21 and m==4 : z = "Aries"
    elif d >= 22 and m==4 or d <=21 and m==5 : z = "Taurus"
    elif d >= 22 and m==5 or d <=21 and m==6 : z = "Gemini"
    elif d >= 22 and m==6 or d <=21 and m==7 : z = "Cancer"
    elif d >= 22 and m==7 or d <=21 and m==8 : z = "Leo"
    elif d >= 22 and m==8 or d <=21 and m==9 : z = "Virgo"
    elif d >= 22 and m==9 or d <=21 and m==10 : z = "Libra"
    elif d >= 22 and m==10 or d <=21 and m==11 : z = "Scorpio"
    elif d >= 22 and m==11 or d <=21 and m==12 : z = "Sagittarius"
    elif d >= 22 and m==12 or d <=20 and m==1 : z = "Capricorn"
    elif d >= 21 and m==1 or d <=20 and m==2 : z = "Aquarius"
    elif d >= 21 and m==2 or d <=21 and m==3 : z = "Pisces"
    return z

def days_in_feb(y) :
    return 29 if y%400 == 0 or y%4 == 0 and y%100 != 0 else 28

def days_in_month(m, y) :
    if m == 2 :     return days_in_feb(y)
    return 30 if m in [4, 6, 9, 11] else 31

def days_in_between(d1, m1, y1, d2, m2, y2) :
    days = 0
    if m1 < 12 : days += 31
    if m1 < 11 : days += 30
    if m1 < 10 : days += 31
    if m1 < 9 : days += 30
    if m1 < 8 : days += 31
    if m1 < 7 : days += 31
    if m1 < 6 : days += 30
    if m1 < 5 : days += 31
    if m1 < 4 : days += 30
    if m1 < 3 : days += 31
    if m1 < 2 : days += days_in_feb(y1)

    if m2 > 1 : days += 31
    if m2 > 2 : days += days_in_feb(y2)
    if m2 > 3 : days += 31 
    if m2 > 4 : days += 30
    if m2 > 5 : days += 31
    if m2 > 6 : days += 30
    if m2 > 7 : days += 31
    if m2 > 8 : days += 31
    if m2 > 9 : days += 30
    if m2 > 10 : days += 31
    if m2 > 11 : days += 30
    days += (days_in_month(m1, y1) - d1 + 1) + int((y2 - y1 - 1)*365.25) + (d2 - 1)
    return days

def main() :
    d1, m1, y1 = read_date()
    d2, m2, y2 = read_date()
    print(zodiac(d1, m1), zodiac(d2, m2))
    print(days_in_between(d1, m1, y1, d2, m2, y2))

exec(input().strip())

# 09_V4
def make_int_list(x) :
    return list(map(int, x.strip().split()))

def is_odd(x) :
    return [False, True][x % 2]

def odd_list(alist) :
    return [x for x in alist if is_odd(x)]

def sum_square(alist) :
    return sum([x**2 for x in alist])

exec(input().strip())