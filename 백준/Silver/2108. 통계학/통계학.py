import sys
input = sys.stdin.readline

N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

def average(nums):
    return round(sum(nums)/len(nums))

def middle(nums):
    m = sorted(nums)
    return m[len(nums)//2]

def frequent(nums):
    temp = [0] * 8001
    idxArr = []

    for i in nums:
        if i >= 0:
            temp[i] += 1
        else:
            i = (-i) + 4000
            temp[i] += 1
        
    maxVal = max(temp)
    maxIdx = temp.index(maxVal)
    if maxIdx > 4000:
        maxIdx = -(maxIdx - 4000)
    idxArr.append(maxIdx)

    for i in range(maxIdx+1, len(temp)):
        if temp[i] == maxVal:
            if i > 4000:
                i = -(i-4000)
            idxArr.append(i)
    
    if len(idxArr) == 1:
        return idxArr[0]
    else:
        idxArr.sort()
        return idxArr[1]

def ranges(nums):
    return max(nums) - min(nums)

print(average(nums))
print(middle(nums))
print(frequent(nums))
print(ranges(nums))