import sys
input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n):
    info = list(input().split())

    age = int(info[0])
    name = info[1]

    arr.append([age, name])

arr.sort(key=lambda x:(x[0]))

for i in range(n):
    print(arr[i][0], arr[i][1])