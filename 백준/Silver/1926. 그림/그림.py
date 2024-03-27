from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]* m for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
q = deque()
max_area = 0
cnt = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            q.append((i,j))
            visited[i][j] = True
            area = 0
            while q:
                x, y = q.popleft()
                area += 1
                block = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                    else:
                        block += 1
                if block == 4:
                    if max_area < area:
                        max_area = area
            cnt += 1

if max_area == 0:
    print(0)
    print(0)
else:
    print(cnt)
    print(max_area)