from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
c = ['push', 'pop', 'size', 'empty', 'front', 'back']
d = deque()

for i in range(n):
    s = list(input().split())
    if s[0] == c[0]:
        d.append(s[1])
    elif s[0] == c[1]:
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif s[0] == c[2]:
        print(len(d))
    elif s[0] == c[3]:
        if d:
            print(0)
        else:
            print(1)
    elif s[0] == c[4]:
        if d:
            print(d[0])
        else:
            print(-1)
    else:
        if d:
            print(d[-1])
        else:
            print(-1)
