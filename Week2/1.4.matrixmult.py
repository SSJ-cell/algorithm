# name: 송성준 
# student id:2020103461  
from typing import List

def matrixmult(n: int, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        U = [[0] * n for i in range(n)]
        for i in range(n) :
            for j in range(n) :
                  for k in range(n) :
                        U[i][j] = A[i][k] * B[k][j]
        return U