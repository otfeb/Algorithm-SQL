n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
s = 0

for i in range(n):
    maxB = max(b)
    s += a[i] * maxB
    b.remove(maxB)

print(s)