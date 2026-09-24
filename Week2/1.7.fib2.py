# name: 송성준 
# student id: 2020103461  
def fib2(n: int) -> int:
    f = [0] * (n + 1)
    # Complete the code here
    if n > 0 :
        f[1] = 1
        for i in range(2, n+1) :
            f[i] = f[i-1] + f[i-2]
    result = f[n]
    return result