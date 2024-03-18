def hanoi(n, a, b, c):      # a:시작 b:도착 c:보조
    if n > 20:
        return
    else:
        if n == 1:
            print(a, b)
            return
        else:
            hanoi(n-1, a, c, b)
            print(a, b)
            hanoi(n-1, c, b, a)

n = int(input())

if n > 20:
    print((2**n)-1)
else:
    print((2**n)-1)
    hanoi(n, 1, 3, 2)