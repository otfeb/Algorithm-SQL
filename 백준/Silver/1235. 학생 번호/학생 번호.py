import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(input()[:-1])

k = 1

while True:
    arr2 = []

    for i in range(n):
        if arr2 and arr[i][-k:] in arr2:
            k += 1
            break
        arr2.append(arr[i][-k:])
    else:
        print(k)
        break