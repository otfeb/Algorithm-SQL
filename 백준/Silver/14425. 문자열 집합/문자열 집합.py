import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
answer = 0

for _ in range(n):
    dic[input()] = 1

for _ in range(m):
    a = input()
    if a in dic and dic[a] == 1:
        answer += 1

print(answer)