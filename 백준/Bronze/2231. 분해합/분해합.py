n = int(input())
result = 0

for i in range(1, n+1):
    producers = list(map(int, str(i)))
    # print(producers)
    result = sum(producers) + i
    if result == n:
        print(i)
        break
else:
    print(0)