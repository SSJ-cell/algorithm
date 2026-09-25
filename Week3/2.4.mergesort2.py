from typing import List

def merge2(low: int, mid: int, high: int, S: List[int]) :
        U = [0]*high
        i, j, k = low, mid+1, 0

        while i <= mid and j <= high :
            if S[i] <= S[j] :
                U[k] = S[i]
                i +=1
            elif S[j] <= S[i] :
                U[k] = S[j]
                j += 1
            k += 1
        if i > mid :
            U[k:] = S[j:high]
        elif j > high :
            U[k:] = S[low:mid+1]   
        S[low:high] = U[:]


def mergesort2(low: int, high: int, S: List[int]) :
        if high > 0 :   
            mid = (low + high) // 2
            mergesort2(low, mid, S)
            mergesort2(mid+1, high, S)
            merge2(low, mid, high, S)