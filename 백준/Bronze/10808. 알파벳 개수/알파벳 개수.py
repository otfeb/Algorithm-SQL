alpa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
answer = [0] * 26
s = input()

for i in range(len(s)):
    for j in range(len(alpa)):
        if s[i] == alpa[j]:
            answer[j] += 1

print(*answer)