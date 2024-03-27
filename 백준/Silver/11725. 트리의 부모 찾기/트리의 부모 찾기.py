import sys
input = sys.stdin.readline
# recursion error 방지
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = [0] * (n+1)
root = 1

for i in range(n-1):
    a, b = map(int,input().split())
    graph[b].append(a)
    graph[a].append(b)

def dfs(a):
    visited[a] = True
    for i in graph[a]:
        if not visited[i]:
            result[i] = a
            dfs(i)

dfs(root)

for i in range(2, n+1):
    print(result[i])