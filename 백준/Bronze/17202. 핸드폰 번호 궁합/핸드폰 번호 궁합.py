import sys
input = sys.stdin.readline
dp = []
a = list(map(int, list(input().rstrip())))
b = list(map(int, list(input().rstrip())))

for i in range(8):
    dp.append(a[i])
    dp.append(b[i])

while len(dp) > 2:
    n = len(dp)
    for i in range(1, n):
        dp.append((dp[i-1]+dp[i]) % 10)
    dp = dp[n:]

print(dp[0], dp[1], sep='')