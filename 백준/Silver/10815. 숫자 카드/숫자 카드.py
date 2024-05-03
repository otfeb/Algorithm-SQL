import sys
input = sys.stdin.readline
n = int(input())
arr = {}

s = list(map(int, input().split()))

for i in s:
    arr[i] = 1

m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    if i in arr:
        print(1, end=' ')
    else:
        print(0, end=' ')