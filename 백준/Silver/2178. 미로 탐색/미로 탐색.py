from collections import deque
import sys
input = sys.stdin.readline
# recursion error 방지
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
# 오른쪽, 왼쪽, 아래, 위
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque([(0,0)])

arr = [[int(i) for i in input().strip()] for _ in range(n)]

while q:
    x, y = q.popleft()

    for i in range(4):
        next_x, next_y = x+dx[i], y+dy[i]
        if 0 <= next_x < n and 0 <= next_y < m:
            if arr[next_x][next_y] == 1:
                q.append((next_x, next_y))
                arr[next_x][next_y] = arr[x][y] + 1

print(arr[n-1][m-1])