s = input()
sLen = len(s)
tmp = 0
slice = 10

while True:
    if sLen >= slice:
        x = s[tmp:slice]
        print(x)
    else:
        x = s[tmp:sLen]
        print(x)
        break
    tmp += 10
    slice += 10