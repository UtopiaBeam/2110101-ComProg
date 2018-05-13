# 11_P1
import numpy as np
data = np.array([[15, 3.78],
                 [29, 2.0],
                 [10, 2.5],
                 [25, 2.85],
                 [30, 3.96]])
logit_pi = -3.98 + 0.2*data[:,0] + 0.5*data[:,1]
p_xi = 1 / (1+np.exp(-logit_pi))
n = int(input())
if not 1 <= n <= 5:     print('Error')
elif p_xi[n-1] > 0.5:   print('True')
else:       print('False')

# 11_P2
import numpy as np
n = int(input())
arr = np.array([float(input().strip().split()[-1]) for _ in range(n)])
mat = np.array([list(map(float, input().strip().split()[1:])) for _ in range(n)])
print(*arr.dot(mat), sep='\n')

# 11_P3
import numpy as np
n = int(input())
for _ in range(3):
    __ = input()
for _ in range(n-3):
    print(np.sum(np.array(input().strip().split(',')[1:], dtype=float)))

# 11_P3 (not using numpy)
for _ in range(int(input())):
    ln = input().strip().split(',')
    if len(ln) == 7 and ln[1].isdigit():
        print(sum(map(float, ln[1:])))

# 11_P4
import numpy as np
def fib(n, k):
    mat = np.array([[0, 1], [1, 1]], dtype=int)
    ans = np.identity(2, dtype=int)
    for _ in range(n):
        ans = ans.dot(mat) % k
    return ans[0,1]
n, k = [int(e) for e in input().split()]
print( fib(n, k) )

# 11_P5
import numpy as np
def fib(n, k):
    if n == 0:      return np.identity(2, dtype=int)
    res = fib(n//2, k)**2
    return [res, np.mat([[0, 1], [1, 1]])*res][n%2] % k
n, k = [int(e) for e in input().split()]
print( fib(n, k)[0,1] )

# 11_P6
import numpy as np
def scale(img, c) :
    nr, nc = img.shape
    return np.array([[img[c*i:c*(i+1), c*j:c*(j+1)].mean() for j in range(nc//c)] for i in range(nr//c)])
def read_img():
    row, col = [int(e) for e in input().split()]
    img = np.ndarray((row,col))
    for i in range(row):
        img[i] = [float(e) for e in input().split()]
    return img
def show_output(out):
    for i in range(out.shape[0]):
        print(" ".join([str(e) for e in out[i]]))
img = read_img()
c = int(input())
out = scale(img, c)
show_output(out)

# 11_P7
import numpy as np
n = int(input())
arr = np.mat([input().strip().split() for _ in range(n)], dtype=int)
res = np.zeros_like(arr, dtype=int)
for i in range(1, n):
    res += arr**i
for row in np.sign(res):
    print(*row)