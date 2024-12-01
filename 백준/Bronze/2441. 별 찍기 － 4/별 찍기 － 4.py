n = int(input())
s = '*' * n

for i in range(n):
    if i < 1:
        print(s)
    else:
        print(s.replace('*', ' ', i))
