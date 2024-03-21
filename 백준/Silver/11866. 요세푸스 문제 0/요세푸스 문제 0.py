from collections import deque
import sys
input = sys.stdin.readline

q = deque()
n, k = map(int, input().split())
arr = []

for i in range(1,n+1):
    q.append(i)

while len(q) > 0:
    for _ in range(k-1):
        x = q.popleft()
        q.append(x)

    y = q.popleft()
    arr.append(y)

result = '<'
delimiter = ','
end = '>'

for i in range(len(arr)):
    if i != len(arr)-1:
        result += str(arr[i])+delimiter+' '
    else:
        result += str(arr[i])+end

print(result)