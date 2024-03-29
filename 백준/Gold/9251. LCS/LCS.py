import sys
input = sys.stdin.readline

first = ' ' + input().rstrip()
second = ' ' + input().rstrip()

dp = [[0] * len(second) for _ in range(len(first))]

for i in range(1, len(first)):
    for j in range(1, len(second)):
        if first[i] == second[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])