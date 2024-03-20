import sys
n = int(sys.stdin.readline())
num = n
count = 0
while True:
    i = num // 10
    j = num % 10
    p = (i + j) % 10
    num = (j * 10) + p
    count += 1
    if num == n:
        break
print(count)