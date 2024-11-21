import sys
import heapq
input = sys.stdin.readline

n = int(input())

positiveNum = []
negativeNum = []

answer = []

for _ in range(n):
    num = int(input())
    
    # pop 명령
    if num == 0:
        if positiveNum and negativeNum:
            if positiveNum[0] < negativeNum[0][0]:
                out = heapq.heappop(positiveNum)
                answer.append(out)
            else:
                out = heapq.heappop(negativeNum)
                answer.append(out[1])
        elif positiveNum:
            out = heapq.heappop(positiveNum)
            answer.append(out)
        elif negativeNum:
            out = heapq.heappop(negativeNum)
            answer.append(out[1])
        else:
            answer.append(0)
    # 양수가 주어졌을 경우
    elif num > 0:
        heapq.heappush(positiveNum, num)
    else:
        heapq.heappush(negativeNum, (-num, num))

for i in answer:
    print(i)