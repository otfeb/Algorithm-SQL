from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    n = [-1, 1, 0, 0, -1, 1, 1, -1]
    m = [0, 0, -1, 1, 1, -1, 1, -1]

    arr[x][y] = 0

    q = deque()
    q.append([x,y])

    while q:
        a, b = q.popleft()
        for i in range(8):
            nx = a + n[i]
            ny = b + m[i]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append([nx,ny])

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [[0 for _ in range(w)] for _ in range(h)]
    landCnt = 0

    for i in range(h):
        line = list(map(int, input().split()))
        for j in range(w):
            arr[i][j] = line[j]

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                bfs(i,j)
                landCnt += 1
    print(landCnt)