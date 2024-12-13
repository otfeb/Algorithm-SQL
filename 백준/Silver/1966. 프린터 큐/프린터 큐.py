import sys
from collections import deque

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    sortedP = sorted(priority, reverse=True)
    idx = 0
    q = deque()
    count = 0

    for ele in enumerate(priority):
        q.append(ele)
    
    while q:
        if q[0][1] != sortedP[idx]:
            out = q.popleft()
            q.append(out)
        else:
            outIdx, outVal = q.popleft()
            idx += 1
            count += 1
            if outIdx == M:
                print(count)
                break