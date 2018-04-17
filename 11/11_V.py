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

# 11_V3 (Incompleted)
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
    return hw[:,1] / cm_to_m(hw[:,0])
def main():
    hw = read_height_weight()
    bmi = cal_bmi(hw)
    avg_bmi = __________________________________
    count_underweight = ________________________
    print('average bmi =', avg_bmi)
    print('#bmi < 18.5 =', count_underweight)
exec(input().strip())