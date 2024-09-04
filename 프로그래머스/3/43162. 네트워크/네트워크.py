def solution(n, computers):
    
    def dfs(x):
        # 방문 처리
        visited[x] = 1
        for i in range(n):
            if computers[x][i] and not visited[i]:
                dfs(i)
    
    answer = 0
    # 방문 배열
    visited = [0 for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer