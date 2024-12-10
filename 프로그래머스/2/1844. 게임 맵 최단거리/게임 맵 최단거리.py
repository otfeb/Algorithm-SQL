from collections import deque

def solution(maps):
    def bfs(a, b):
        flag = False
        q = deque([(a, b)])
        while q:
            x, y = q.popleft()
            if x == n-1 and y == m-1:
                flag = True
                return maps[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[nx][ny] == 1:
                    q.append((nx,ny))
                    maps[nx][ny] = 1 + maps[x][y]
        return -1
    
    n = len(maps)
    m = len(maps[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    answer = bfs(0, 0)
    
    return answer