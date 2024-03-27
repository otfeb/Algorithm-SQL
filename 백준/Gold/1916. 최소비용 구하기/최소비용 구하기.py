import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
node = [[] for _ in range(n+1)]
dis = [float('inf')] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    node[a].append((b, c))

start, end = map(int,input().split())

queue = [(0,start)]
heapq.heapify(queue)

dis[start] = 0

while queue:
    cost, now = heapq.heappop(queue)
    visited[now] = True

    if dis[now] < cost:
        continue
 
    for i,j in node[now]:
        if not visited[i]:
            if dis[i] > j + dis[now]:
                dis[i] = j + dis[now]
                heapq.heappush(queue, (dis[i], i))

print(dis[end])