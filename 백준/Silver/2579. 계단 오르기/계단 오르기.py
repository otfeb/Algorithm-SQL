import sys
input = sys.stdin.readline
n = int(input())
score = [0]
max_num = 0

for _ in range(1, n+1):
    score.append(int(input()))

if n == 1:
    print(score[1])
else:
    dp = [[0] * 3 for _ in range(n+1)]
    dp[1][1] = score[1]
    dp[1][2] = 0
    dp[2][1] = score[2]
    dp[2][2] = score[1] + score[2]

    for i in range(3, n+1):
        for j in range(1, 3):
            if j == 1:
                dp[i][j] = max(dp[i-2][1], dp[i-2][2]) + score[i]
            else:
                dp[i][j] = dp[i-1][1] + score[i]
    print(max(dp[n][1], dp[n][2]))