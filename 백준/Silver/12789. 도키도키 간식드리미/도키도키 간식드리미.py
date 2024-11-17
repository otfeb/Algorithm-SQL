import sys
from collections import deque

n = sys.stdin.readline()
students = list(map(int, sys.stdin.readline().split()))

q = deque(students)
stack = []

while q:
    snack = min(q)

    if stack:
        stackPeek = stack[-1]
        if stackPeek < snack:
            stack.pop()
            break

    curr = q.popleft()

    if curr != snack:
        stack.append(curr)

while stack:
    curr = stack.pop()
    
    if stack and curr > stack[-1]:
        print("Sad")
        break

else:
    print("Nice")