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