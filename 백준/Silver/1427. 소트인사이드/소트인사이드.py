import sys
input = sys.stdin.readline

n = list(map(int, input().rstrip()))
n.sort()
n.reverse()

for i in n:
    print(i, end='')