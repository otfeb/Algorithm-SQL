import sys
input = sys.stdin.readline
from collections import deque
# recursion error 방지
sys.setrecursionlimit(10**9)

q = deque()
n, m, v = map(int, input().split())
arr = [[False] * (n+1) for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    arr[a][b] = True                    # 무방향 그래프이기 때문에
    arr[b][a] = True

visited1 = [False] * (n+1)
visited2 = visited1.copy()

# dfs
def dfs(v):
    visited1[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        # v노드와 연결된 노드고, 아직 방문 안했을 경우
        if arr[v][i] == True and visited1[i] == False:
            dfs(i)

# bfs
def bfs(v):
    q.append(v)
    visited2[v] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if arr[v][i] == True and visited2[i] == False:
                q.append(i)
                visited2[i] = True

dfs(v)
print()
bfs(v)