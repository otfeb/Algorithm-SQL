import sys

n = int(input())
stack = []

for i in range(n):
    cmd = list(map(int, sys.stdin.readline().split()))

    if cmd[0] == 1:
        stack.append(cmd[1])
    elif cmd[0] == 2:
        if stack:
            out = stack.pop()
            print(out)
        else:
            print(-1)
    elif cmd[0] == 3:
        print(len(stack))
    elif cmd[0] == 4:
        if not stack:
            print(1)
        else:
            print(0)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)