from collections import deque
n = int(input())
q = deque()

for i in range(1, n+1):
    q.append(i)

while len(q) > 1:
    q.popleft()
    move = q.popleft()
    q.append(move)

print(q[0])