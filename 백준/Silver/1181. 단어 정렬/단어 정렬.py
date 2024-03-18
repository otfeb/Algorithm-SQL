import sys
input = sys.stdin.readline

n = int(input())
arr = []
temp = ''

for i in range(n):
    s = input()

    if temp != s:
        temp = s
        arr.append(s[:len(s)-1])

arr2 = set(arr)
arr = list(arr2)
arr.sort()

result = []

maxL = len(max(arr, key=len))

for i in range(maxL+1):
    for j in range(len(arr)):
        if len(arr[j]) == i:
            result.append(arr[j])

for i in result:
    print(i)