import sys
input = sys.stdin.readline

while True:
    x = input()
    if x == '0\n':
        break
    s = list(x[:-1])
    a = list(reversed(s))

    for i in range(len(s)):
        if s[i] != a[i]:
            print('no')
            break
    else:
        print('yes')