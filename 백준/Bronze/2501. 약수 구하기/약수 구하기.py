n, k = map(int, input().split())

divisor = 0

for i in range(1, n+1):
    if n % i == 0:
        divisor += 1
        if divisor == k:
            print(i)

if divisor < k:
    print(0)