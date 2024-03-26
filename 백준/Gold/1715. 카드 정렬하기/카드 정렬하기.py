import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
sum = 0
result = 0

if len(arr) == 1:
    print(0)
elif len(arr) == 2:
    print(arr[0] + arr[1])
else:
    heapq.heapify(arr)
    pop = heapq.heappop(arr)
    pop2 = heapq.heappop(arr)
    sum = pop + pop2
    result += sum
    while arr:
        heapq.heappush(arr, sum)
        pop = heapq.heappop(arr)
        pop2 = heapq.heappop(arr)
        sum = pop + pop2
        result += sum

    print(result)