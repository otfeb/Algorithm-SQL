from itertools import permutations
import sys
 
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
 
per = permutations(A)
ans = 0
 
for i in per:
    s = 0
    for j in range(len(i)-1):
        s += abs(i[j]-i[j+1])
    if s > ans:
        ans = s
 
print(ans)