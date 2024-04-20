import sys
input = sys.stdin.readline
cnt = 0
n = int(input())
cards = list(map(int, input().split()))

m = int(input())
compareCards = list(map(int, input().split()))

count = {}

for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for target in compareCards:
    result = count.get(target)
    if result == None:
        print(0, end=' ')
    else:
        print(result, end=' ')