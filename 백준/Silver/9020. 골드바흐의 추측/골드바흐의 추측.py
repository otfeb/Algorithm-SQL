import sys

def isPrime(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def gold(a):
    x = a//2

    for i in range(x,0,-1):
        if isPrime(i):
            if isPrime(a-i):
                nums = [i, a-i]
                return nums

t = int(sys.stdin.readline())
nums = [0]*2

for i in range(t):
    n = int(sys.stdin.readline())
    nums = gold(n)
    list.sort(nums)
    print(nums[0], nums[1])
    

