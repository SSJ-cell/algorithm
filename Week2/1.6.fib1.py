# name: 송성준 
# student id: 2020103461  
def fib1(n: int) -> int:
    # Complete the code here
    if n <= 1 :
        return n
    else :
        return fib1(n-1) + fib1(n-2)