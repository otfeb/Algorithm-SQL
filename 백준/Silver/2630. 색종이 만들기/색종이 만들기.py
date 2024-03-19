import sys
input = sys.stdin.readline

white, blue = 0, 0

def cut(x, y, n):
    global white, blue
    color = arr[x][y]       # 첫 번째 색

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:                  # 처음과 색이 다르면 분할
                cut(x, y, n //2)                    # 1사분면
                cut(x, y + n//2, n //2)             # 2사분면
                cut(x + n//2, y, n //2)             # 3사분면
                cut(x + n//2, y + n//2, n //2)      # 4사분면
                return
            
    if color == 0:                                  # 모두 같은 색이면 0 or 1 판별
        white += 1
    else:
        blue += 1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cut(0,0,n)
print(white, blue, sep='\n')

