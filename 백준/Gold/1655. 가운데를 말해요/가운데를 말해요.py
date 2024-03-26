import heapq
import sys
input = sys.stdin.readline

n = int(input())
letfHeap = []
rightHeap = []

for i in range(n):
    num = int(input())

    if len(letfHeap) == len(rightHeap):
        heapq.heappush(letfHeap, -num)
    else:
        heapq.heappush(rightHeap, num)

    if rightHeap and rightHeap[0] < -letfHeap[0]:
        leftValue = heapq.heappop(letfHeap)
        rightValue = heapq.heappop(rightHeap)
        heapq.heappush(letfHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)

    print(-letfHeap[0])