import sys
input = sys.stdin.readline
# recursion error 방지
sys.setrecursionlimit(10**9)

n = int(input())
m = int(input())

network = [[False] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    network[a][b] = network[b][a] = True

visited = [False] * (n+1)
cnt = 0

def dfs(v):
    global cnt
    visited[v] = True

    for i in range(1, n+1):
        if network[v][i] and not visited[i]:
            cnt += 1
            dfs(i)

dfs(1)
print(cnt)