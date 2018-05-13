# 11_V1
print('dbdad'[int(input())-1])

# 11_V2
import numpy as np
arr = np.array(list(map(int, input().split())))
mat = np.array([
    [float(x) for x in input().split()] for _ in range(4)
])
mx = max(range(5), key = lambda x: sum(mat[:,x]))
print(['Mon', 'Tue', 'Wed', 'Thu', 'Fri'][mx], sum(mat[:,mx]))
print(*np.dot(arr, mat))

# 11_V3
import numpy as np
def read_height_weight():
    list_hw = []
    for k in range(int(input())) :
        h,w = input().split()
        list_hw.append((int(h),int(w)))
    return np.array(list_hw)
def cm_to_m(x):
    return x/100
def cal_bmi(hw):
    return hw[:,1] / cm_to_m(hw[:,0])**2
def main():
    hw = read_height_weight()
    bmi = cal_bmi(hw)
    avg_bmi = bmi.mean()
    count_underweight = (bmi < 18.5).sum()
    print('average bmi =', avg_bmi)
    print('#bmi < 18.5 =', count_underweight)
exec(input().strip())

# 11_V4
import numpy as np
def read_square_matrix():
    d = [int(e) for e in input().split()]
    m = [d]
    for k in range(len(d)-1):
        m.append([int(e) for e in input().split()])
    return np.array(m)
def min_in_each_row(m):
    return np.min(m, axis=1)
def max_in_each_column(m):
    return np.max(m, axis=0)
def diff_of_sums_of_two_diags(m):
    return abs(np.diag(m).sum() - np.diag(m[::-1, :]).sum())
def halve(m):
    return m[::2, ::2] + m[1::2, ::2] + m[::2, 1::2] + m[1::2, 1::2]
exec(input().strip())