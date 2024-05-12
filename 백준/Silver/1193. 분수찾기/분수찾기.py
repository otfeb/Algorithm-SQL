import sys
input = sys.stdin.readline
x = int(input())
line = 1

# 대각선 라인 구하기
while x > line:
    x -= line
    line += 1

# 짝수일 경우
if line % 2 == 0:
    a = x
    b = line - x + 1
# 홀수일 경우
else:
    a = line - x + 1
    b = x

print(f'{a}/{b}')