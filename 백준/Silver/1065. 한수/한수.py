def han(a):

    x = a//100          # 100의 자리
    y = (a%100)//10     # 10의 자리
    z = a%10            # 1의 자리

    if a < 100:
        return True
    elif x - y == y - z or z - y == y - x:
        return True
    
cnt = 0
n = int(input())

for i in range(1,n+1):
    if han(i):
        cnt += 1

print(cnt)
    
        