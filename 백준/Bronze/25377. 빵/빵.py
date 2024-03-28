import sys
input = sys.stdin.readline

n = int(input())
min = 1000
no = 0

for i in range(n):
    x, y = map(int, input().split())
    if x > y:
        no += 1
    else:
        if min > y:
            min = y
if no == 3:
    print(-1)
else:
    print(min)