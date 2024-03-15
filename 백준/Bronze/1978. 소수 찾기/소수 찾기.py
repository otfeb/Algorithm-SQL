def prime(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True
        
n = int(input())
cnt = 0

t = list(map(int, input().split()))

for i in t:
    if prime(i):
        cnt += 1

print(cnt)




