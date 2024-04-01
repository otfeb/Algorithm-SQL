import sys
input = sys.stdin.readline

a = list(input().rstrip().split('-'))
temp = []

for i in range(len(a)):
    b = list(map(int, a[i].split('+')))
    temp.append(sum(b))

result = temp[0]

for i in range(1, len(temp)):
    result -= temp[i]

print(result)