from collections import deque

def solution(n, computers):
    
    def bfs(x):
        queue = deque()
        queue.append(x)
        while queue:
            a = queue.popleft()
            visited[a] = 1
            for i in range(n):
                if computers[a][i] and not visited[i]:
                    queue.append(i)
    
    answer = 0
    visited = [0 for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    
    return answer