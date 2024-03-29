import sys
input = sys.stdin.readline

string_a = ' ' + input().rstrip()
string_b = ' ' + input().rstrip()

dp = [[''] * len(string_b) for _ in range(len(string_a))]

for i in range(1, len(string_a)):
    for j in range(1, len(string_b)):
        if string_a[i] == string_b[j]:
            dp[i][j] = dp[i-1][j-1] + string_a[i]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
result = dp[-1][-1]
print(len(result), result, sep='\n')