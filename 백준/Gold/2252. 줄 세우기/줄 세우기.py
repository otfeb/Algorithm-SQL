from collections import deque
import sys
input = sys.stdin.readline
# recursion error 방지
sys.setrecursionlimit(10**9)

q = deque()
n, m = map(int, input().split())
order = [0] * (n+1)                          # 진입 차수 배열
line = [[] for _ in range(n+1)]
sort_arr = []

for _ in range(m):
    a, b = map(int, input().split())
    line[a].append(b)
    order[b] += 1

for i in range(1, n+1):
    if order[i] == 0:
        q.append(i)

while q:
    temp = q.popleft()
    sort_arr.append(temp)
    for i in line[temp]:
        order[i] -= 1
        if order[i] == 0:
            q.append(i)

print(*sort_arr)