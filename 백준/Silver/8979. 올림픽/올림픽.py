import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [[0 for _ in range(5)] for _ in range(n)]

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(4):
        arr[i][j] = temp[j]

arr.sort(key=lambda x : (x[1], x[2], x[3]), reverse=True)

arr[0][4] = 1

for i in range(1, n):
    if arr[i][1:4] != arr[i-1][1:4]:
        arr[i][4] = arr[i-1][4] + 1
    else:
        arr[i][4] = arr[i-1][4]

rank = 0

for i in range(n):
    if k == arr[i][0]:
        rank = arr[i][4]
        break

print(rank)