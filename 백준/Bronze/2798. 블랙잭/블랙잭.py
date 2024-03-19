import sys
imput = sys.stdin.readline

result = 0
n, m = map(int, input().split())
arr = list(map(int, input().split()))

found = False
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and i != k:
                sum = arr[i]+arr[j]+arr[k]
                if sum <= m and result < sum:
                    result = sum
                if result == m:
                    found = True
                    break
        if found:
            break
    if found:
        break

print(result)