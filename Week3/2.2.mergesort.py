from typing import List

def merge(h: int, m: int, U: List[int], V: List[int], S: List[int]) -> None:
    assert sorted(U) == U
    assert sorted(V) == V
    
    i = j = k = 0
    # Complete the code here
    while i < h and j < m :
        if U[i] < V[j] :
            S[k] = U[i]
            i += 1
        else :
            S[k] = V[j]
            j += 1
        k += 1
    if i == h :
        S[k:] = V[j:]
    elif j == m :
        S[k:] = U[i:]
    

def mergesort(n: int, S: List[int]) -> None:
    h = n // 2
    m = n - h
    if n > 1:
        # Complete the code here
        U = S[:h]
        V = S[h:]
        mergesort(h, U)
        mergesort(m, V)
        merge(h, m, U, V, S)
