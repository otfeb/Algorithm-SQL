import sys
input = sys.stdin.readline

dic = {}
answer = []
n, m = map(int, input().split())

for _ in range(n):
    s = input()
    dic[s[:-1]] = "NO_LISTEN"

for _ in range(m):
    s = input()
    if s[:-1] in dic and dic[s[:-1]] == "NO_LISTEN":
        answer.append(s[:-1])

answer.sort()
print(len(answer))
for i in answer:
    print(i)