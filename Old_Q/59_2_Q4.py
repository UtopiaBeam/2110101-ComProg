# 59_2_Q4_2_p (Some parts of the program)
def S(n, k): 
    if n == k:      return 1
    if k == 0:      return 0
    return S(n-1, k-1) - (n-1)*S(n-1, k)
    
def L(x, y, i, j):       
    if i == -1 or j == -1:      return 0
    if x[i] == y[j]:    return 1 + L(x, y, i-1, j-1)
    return max(L(x, y, i-1, j), L(x, y, i, j-1))
    
def P(n, k):
    if n <= k:      return k
    if k%2 == 0:
        tmp = P(n, k+1)
        return 2 + tmp + (tmp % 789)
    return P(n, k+3) - 5
    
def Hanoi(n, L, M, R):   
    if n == 1:      print(1, L, '->', R)
    else:
        Hanoi(n-1, L, R, M)
        print(n, L, '->', R)
        Hanoi(n-1, M, L, R)

# 59_2_Q4_3_p
import numpy as np
def to_polar(p):
    X, Y = p[:, 0], p[:, 1]
    rt = np.ndarray(p.shape)
    rt[:, 0] = np.sqrt(X**2+Y**2)
    rt[:, 1] = np.arctan2(Y,X)
    return rt
def to_cartesian(p):
    R, T = p[:, 0], p[:, 1]
    xy = np.ndarray(p.shape)
    xy[:, 0] = R*np.cos(T)
    xy[:, 1] = R*np.sin(T)
    return xy
def mandel( h, w, m ):
    y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
    c = x+y*1j
    z = c
    dt = m + np.zeros(z.shape, dtype=int)
    for i in range(m):
        z = z**2 + c
        di = z*np.conj(z) > 2**2
        dn = di & (dt==m)
        dt[dn] = i
        z[di] = 2
    return dt
def merge( dt, m ):
    x = dt[m ,:]
    y = dt[:, m]
    xy = [[x[k], y[k]] for k in range(len(x))]
    xy = np.array(xy, float)
    return xy
def main():
    h1, w1, m1 = [int(e) for e in input().split()]
    h2, w2, m2 = [int(e) for e in input().split()]
    dt1 = mandel(h1, w1, m1)
    xy1 = merge(dt1, m1)
    rt1 = to_polar(xy1)
    rt1[:, 1] += 0.5
    xy1 = to_cartesian(rt1)
    
    dt2 = mandel(h2, w2, m2)
    xy2 = merge(dt2, m2)
    xy2[:, 1] += 0.5
    xy2 = to_cartesian(xy2)
    print(np.sum(xy1.dot(xy2.T)))
exec(input().strip())

# 59_2_Q4_4_p
import numpy as np
def decode(c, base, oddonly):
    mat = np.array([base**i * c[::-1,:][i,:] for i in range(c.shape[0])])
    res = np.sum(mat , axis=0)
    return res[1::2] if oddonly else res
exec(input().strip())
exec(input().strip())
exec(input().strip())