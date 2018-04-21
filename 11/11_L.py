# 11_L1
print('acbcb'[int(input())-1])

# 11_L2
import numpy as np
def all_pair_distances(p):
    x, y = p[:, 0], p[:, 1]
    X, Y = np.array([x]), np.array([y])
    dX, dY = X - X.T, Y - Y.T
    return np.hypot(dX, dY)
exec(input().strip())

# 11_L3
import numpy as np
def eval_poly(x, coef):
    Y = x * np.ones_like(coef)
    Y[0] = 1
    Y = np.cumprod(Y)
    return np.sum(coef*Y, dtype=float)
exec(input().strip())

# 11_L4
import numpy as np
def checker(n):
    arr = np.array([np.zeros(n)], dtype=int)
    arr[:, 1::2] = 1
    return arr ^ arr.T
def collide(e, C):
    return C[ np.sum((e[:2] - C[:, :2])**2, axis=1) <= (e[2]+C[:,2])**2 ]
def matrix_chain_mult(M, order):
    ans = M[order[0]]
    for i in order[1:]:
        ans = ans.dot(M[i]) if i > order[0] else M[i].dot(ans)
    return ans
exec(input().strip())