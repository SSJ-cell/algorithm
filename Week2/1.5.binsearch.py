# name: 송성준 
# student id: 준2020103461 
from typing import List

def binsearch(n: int, S: List[int], x: int) -> int:
    low = 0
    high = n-1

    while low <= high :
        mid = (low + high) // 2
        if S[mid] == x :
            return mid
        elif S[mid] < x :
            low = mid + 1
        else :
            high = mid - 1
    return -1