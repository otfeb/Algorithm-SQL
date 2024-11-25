import itertools, sys
input = sys.stdin.readline

lotto = 6

while True:
    line = input()

    if line == "0\n":
        break

    process = list(map(int, line.split()))
    k = process[0]
    s = process[1:]

    startLotto = itertools.combinations(s, lotto)

    for i in list(startLotto):
        for j in range(lotto):
            print(i[j], end=' ')
        print()
    print()