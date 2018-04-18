# Sample_Q4_2a
import numpy as np
def H(n):
    if n == 1:      return np.array([[1]])
    tmp = H(n-1)
    return np.array([np.concatenate([ls, ls]) for ls in tmp] + [np.concatenate([ls, -1*ls]) for ls in tmp])
def P(n):   return 1 if n == 1 else 3*P(n-1) + M(n-1)
def M(n):   return 0 if n == 1 else 3*M(n-1) + P(n-1)
def S(n):   return P(n) - M(n)
exec(input().strip())

# Sample_Q4_2b
def F(n):
    if n <= 2:      return [0, 1, 1][n]
    x = F(n//3)
    if n % 3 == 0:      return 5*x**3 + 3*(-1)**n*x
    t = F(n//3 + 1)
    if n % 3 == 1:      return t**3 + 3*t*x**2 - x**3
    return t**3 + 3*x*t**2 + x**3
def x(m, n):
    if m*n == 0:    return m+n
    return x(m-1, n) + x(m, n-1)
def p(n):
    if n <= 1:      return n
    if n % 2 == 0:  return n + 2*p(n-1) + p(n-2)
    return n + p(n-1) + 2*p(n-2)
def z1(n):
    return z1(z2(n)) + z2(n) if n >= 10 else z2(n)
def z2(n):
    return n if n < 10 else n%10 + z2(n//10)
exec(input().strip())

# Sample_Q4_3
def remove_symbol(s):
    symbol, s2 = '0123456789+-,./!', ''
    for c in s:
        if c in symbol:     s2 += ' '
        else:       s2 += c.lower()
    return s2
def str_to_unique_list(s):
    ls = []
    for st in s.split():
        if st.strip() not in ls:
            ls.append(st.strip())
    return ls
def percent_in_list(template, test):
    count = 0
    for w in test:
        if w in template:   count += 1
    return count*100/len(test)
def main():
    good = input().strip()
    good_list = str_to_unique_list(remove_symbol(good))
    bad = input().strip()
    bad_list = str_to_unique_list(remove_symbol(bad))
    n = int(input())
    for _ in range(n):
        test = input().strip()
        test_list = str_to_unique_list(remove_symbol(test))
        good_p = percent_in_list(good_list, test_list)
        bad_p = percent_in_list(bad_list, test_list)
        print(test_list)
        print(good_p, bad_p)
exec(input().strip())

# Sample_Q4_4
import numpy as np
def read_matrix():
    r,c = [int(e) for e in input().split()]
    m = [[int(e) for e in input().split()] for i in range(r)]
    return np.array(m)
def dot_row_column(m):
    return m.dot(m)
def mul_submatrix(m, n):
    r, c, k = *m.shape, n.shape[0]
    return np.array([[x for j in range(c//k) for x in m[i, k*j:k*(j+1)].dot(n)] for i in range(r)])
def resize(m, a, b):
    r, c = m.shape
    return np.tile(m, ((a-1)//r+1, (b-1)//c+1) )[:a, :b]
exec(input().strip())