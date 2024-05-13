n = int(input())
cnt = 1
sequence = 6

while n > 0 and n != 1:
    n -= sequence
    cnt += 1
    sequence += 6

print(cnt)