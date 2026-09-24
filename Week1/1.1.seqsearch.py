from typing import List

def seqsearch(n: int, S: List[int], x: int) -> int :
    location = -1
    for i in range(n) :
        if S[i] == x :
            location = i
    return location