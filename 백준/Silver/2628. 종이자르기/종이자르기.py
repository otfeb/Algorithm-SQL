x, y = map(int, input().split())
t = int(input())

maxW = 0        # 가로
maxL = 0        # 세로

arrW = [0, x]
arrL = [0, y]

for i in range(t):
    a,b = map(int, input().split())
    if a == 0:
        arrL.append(b)  
    else:
        arrW.append(b)

list.sort(arrW)
list.sort(arrL)

for i in range(1,len(arrW)):
    if maxW < arrW[i] - arrW[i-1]:
        maxW = arrW[i] - arrW[i-1]

for i in range(1,len(arrL)):
    if maxL < arrL[i] - arrL[i-1]:
        maxL = arrL[i] - arrL[i-1]

print(maxW*maxL)

