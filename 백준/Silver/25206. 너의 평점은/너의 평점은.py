scoreDict = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
total = 0.0     # (학점 * 평점) 총합
sum = 0.0       # 학점 총합

for i in range(20):
    s = input().split()
    grade = float(s[1])
    score = s[2]

    if score == 'P':
        continue
    else:
        total += grade * scoreDict[score]
        sum += grade

if sum == 0.0:
    print(f"{total:6f}")
else:
    #print(round(total/sum, 6))
    print(f"{total/sum:6f}")