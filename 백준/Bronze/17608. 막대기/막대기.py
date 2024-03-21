import sys
input = sys.stdin.readline

n = int(input())
stick = []

for i in range(n):
    s = int(input())
    stick.append(s)

last = stick[-1]
cnt = 1
preStick = 0

for i in range(n-1, -1, -1):
    if stick[i] > last and stick[i] > preStick:
        cnt += 1
        preStick = stick[i]

print(cnt)