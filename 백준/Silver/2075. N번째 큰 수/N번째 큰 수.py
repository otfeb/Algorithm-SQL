import sys
import heapq
input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n):
    lines = list(map(int, input().split()))
    for line in lines:
        if len(arr) < n:
            heapq.heappush(arr, line)
        else:
            if arr[0] < line:
                heapq.heappop(arr)
                heapq.heappush(arr, line)

print(arr[0])