import sys
input = sys.stdin.readline

n = int(input())
conference_time = []
cnt = 1

for i in range(n):
    start, end = map(int, input().split())
    conference_time.append((start, end))

sort_conference = sorted(conference_time, key=lambda x: (x[1], x[0]))

x = sort_conference[0][0]
y = sort_conference[0][1]

for i in range(1, n):
    if sort_conference[i][0] < y:
        continue
    else:
        cnt += 1
        y = sort_conference[i][1]

print(cnt)