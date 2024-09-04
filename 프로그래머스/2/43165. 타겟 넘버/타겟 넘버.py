def dfs(index, cur_sum, numbers, target):
    global ans
    
    if index == len(numbers):
        if cur_sum == target:
            ans += 1
            return
        return
    
    dfs(index+1, cur_sum+numbers[index], numbers, target)
    dfs(index+1, cur_sum-numbers[index], numbers, target)

def solution(numbers, target):
    global ans
    ans = 0
    dfs(0,0,numbers,target)
    return ans