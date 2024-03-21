import sys
input = sys.stdin.readline

k = int(input())
result = []

for i in range(k):
    n = int(input())
    if n != 0:
        result.append(n)
    else:
        if len(result) != 0:
            result.pop()
        
sum = 0

for i in result:
    sum += i
print(sum)