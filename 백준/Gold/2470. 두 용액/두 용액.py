import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

sumArr = []
left = 0
right = n-1
min = sys.maxsize

while left < right:
    sum = arr[left] + arr[right]
    if abs(sum) <= min:
        min = abs(sum)
        sumArr = [arr[left], arr[right]]
    
    if sum > 0:
        right -= 1
    elif sum < 0:
        left += 1
    else:
        break

for i in sumArr:
    print(i, end=' ')