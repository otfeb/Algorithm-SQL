import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    grade = []
    top = 0
    result = 0
    n = int(input())
    for j in range(n):
        a, b = map(int, input().split())
        grade.append((a, b))

    grade.sort()
    top = grade[0][1]
    result += 1

    for j in range(n):
        if grade[j][1] < top:
            result += 1
            top = grade[j][1]

    print(result)