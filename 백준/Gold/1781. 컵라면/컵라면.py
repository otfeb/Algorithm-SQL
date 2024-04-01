import sys, heapq
input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort()

queue = []

for i in arr:
    heapq.heappush(queue, i[1])
    if i[0] < len(queue):
        heapq.heappop(queue)

print(sum(queue))