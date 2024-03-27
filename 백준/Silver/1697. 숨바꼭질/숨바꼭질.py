import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
visited = [0] * 100001

def bfs(a):
    q = deque([a])
    while q:
        node = q.popleft()
        if node == k:
            return visited[node]
        for i in (node-1, node+1, node*2):
            if 0 <= i < 100001 and visited[i] == 0:
                visited[i] = visited[node] + 1
                q.append(i)

print(bfs(n))