import math

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = math.factorial(m)
    b = math.factorial(n)
    c = math.factorial(m-n)
    print(a//(b*c))