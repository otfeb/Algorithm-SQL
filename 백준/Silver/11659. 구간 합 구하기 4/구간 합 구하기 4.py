import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sumArr = [0] * (n + 1)

for i in range(1, n+1):
    sumArr[i] = sumArr[i-1] + arr[i-1]

for i in range(m):
    a, b = map(int, input().split())
    print(sumArr[b] - sumArr[a-1])