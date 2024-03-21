import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    result = []
    cnt = 0
    p = input()
    p = list(p.strip('\n'))
    for j in range(len(p)):
        if cnt < 0:
            break
        if j == 0:
            if p[j] == ')':
                cnt += 1
                break
        if p[j] == '(':
            result.append(p[j])
            cnt += 1
        elif p[j] == ')':
            result.append(p[j])
            cnt -= 1
    if cnt == 0:
        print('YES')
    else:
        print('NO')