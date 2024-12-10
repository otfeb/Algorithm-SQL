from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    answer = bfs(begin, target, words)
    
    return answer

def bfs(begin, target, words):
    q = deque()
    q.append([begin, 0])
    while q:
        now, step = q.popleft()
        if now == target:
            break
        for word in words:
            cnt = 0
            for i in range(len(word)):
                if now[i] != word[i]:
                    cnt += 1
            if cnt == 1:
                q.append([word, step+1])
    answer = step
    return answer