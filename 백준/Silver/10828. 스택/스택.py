import sys
input = sys.stdin.readline

c = int(input())
command = ['push', 'pop', 'size', 'empty', 'top']
result = []

for i in range(c):
    line = list(input().split())
    if line[0] == command[0]:
        result.append(line[1])
    elif line[0] == command[1]:
        if len(result) != 0:
            print(result.pop())
        else:
            print(-1)
    elif line[0] == command[2]:
        print(len(result))
    elif line[0] == command[3]:
        if len(result) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(result) != 0:
            print(result[-1])
        else:
            print(-1)