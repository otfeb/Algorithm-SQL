import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# arr보다 index가 1씩 더 큼
perfixSum = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        perfixSum[i][j] = perfixSum[i-1][j] + perfixSum[i][j-1] - perfixSum[i-1][j-1] + arr[i-1][j-1]


k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(perfixSum[x][y] - (perfixSum[x][j-1] + perfixSum[i-1][y]) + perfixSum[i-1][j-1])