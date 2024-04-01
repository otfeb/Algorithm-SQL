import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
cnt = 0

for i in range(n):
    coins.append(int(input()))

for i in reversed(range(n)):
    cnt += k // coins[i]
    k %= coins[i]

print(cnt)