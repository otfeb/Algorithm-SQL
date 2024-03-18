import sys
import itertools
input = sys.stdin.readline

target = 100

def brute_force(arr):

    global target
    arr = sorted(arr)

    nPr = list(itertools.permutations(arr, 7))

    for i in range(len(nPr)):
        if sum(nPr[i]) == target:
            return nPr[i]
    
arr = [int(input()) for _ in range(9)]

result = brute_force(arr)

for i in result:
    print(i)