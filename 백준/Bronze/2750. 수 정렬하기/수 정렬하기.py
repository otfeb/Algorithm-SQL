import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    d_left = merge_sort(left)
    d_right = merge_sort(right)
    return merge(d_left, d_right)

def merge(left, right):
    i, j = 0, 0
    sorted_list = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < len(left):                    # 정렬 후 남은 데이터 sorted_list에 넣기
        sorted_list.append(left[i])         # left 나 right 리스트중 하나가 먼저 정렬되었을 경우
        i += 1                              # 한쪽에 남아있는 데이터를 마저 옮겨준다
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    return sorted_list

n = int(input())
arr = [int(input()) for _ in range(n)]
arr = merge_sort(arr)

for i in arr:
    print(i)