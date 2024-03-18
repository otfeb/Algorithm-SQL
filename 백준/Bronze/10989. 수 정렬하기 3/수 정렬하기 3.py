import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001                                  # 배열값 모두 0으로 초기화

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1            # 입력값에 해당하는 index에 1씩 대입

for i in range(10001):
    if num_list[i] != 0:                                # 값이 0인 index를 제외한
        for j in range(num_list[i]):                    # 만약 num_list[3]의 값이 2이면 두번 출력
            print(i)