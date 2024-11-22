import sys
input = sys.stdin.readline

a, b = input().split()
count = 0

if a == b:
    print(0)
elif len(a) == len(b):
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    print(count)
else:
    if a == "":
        print(len(b))
    elif b == "":
        print(len(a))
    else:
        lengthA = len(a)
        lenghtB = len(b)

        side = 0
        min = 51

        while side + lengthA <= lenghtB:
            count = 0

            for i in range(lengthA):
                if a[i] != b[i+side]:
                    count += 1
            if min > count:
                min = count
            side += 1
        print(min)