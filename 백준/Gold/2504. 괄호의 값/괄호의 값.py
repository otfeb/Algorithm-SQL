s = list(input())

cnt = 1
result = 0
stack = []

for i in range(len(s)):
    if s[i] == '(':
        cnt *= 2
        stack.append(s[i])
    elif s[i] == '[':
        cnt *= 3
        stack.append(s[i])
    elif s[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if s[i-1] == '(':
            result += cnt
        cnt //= 2
        stack.pop()
    else:
        if not stack or stack[-1] == '(':
            result = 0
            break
        if s[i-1] == '[':
            result += cnt
        cnt //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)