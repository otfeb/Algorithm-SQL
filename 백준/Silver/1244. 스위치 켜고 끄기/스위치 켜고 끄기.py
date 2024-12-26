import sys
input = sys.stdin.readline

n = int(input())
status = list(map(int, input().split()))
k = int(input())

# 스위치 상태 변경
def switch(a):
    if status[a] == 1:
        status[a] = 0
    else:
        status[a] = 1

# 학생 받으면서 스위치 변경 시작
for _ in range(k):
    gender, num = map(int, input().split())

    if gender == 1:
        for i in range(1, n+1):
            if i % num == 0:
                switch(i-1)
    else:
        prev = num - 2
        next = num
        switchArr = [num-1]

        while prev >= 0 and next < n:
            if status[prev] != status[next]:
                break
            switchArr.append(prev)
            switchArr.append(next)
            prev -= 1
            next += 1
        
        for i in switchArr:
            switch(i)

for i in range(1, n+1):
    if i != 1 and i % 20 == 1:
        print()
    print(status[i-1], end=' ')