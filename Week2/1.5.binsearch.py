# name: 송성준 
# student id: 준2020103461 
from typing import List

def binsearch(n: int, S: List[int], x: int) -> int:
    low, high = 0, n - 1
    location = -1

    # Complete the code here
    while low <= high :
        mid = (high + low)//2
        if S[mid] == x :
            location = mid
            break
        elif S[mid] > x :
            high = mid - 1
        elif S[mid] < x :
            low = mid + 1
        
    return location
