import sys

while True:
    stack = []
    answer = ""

    input = sys.stdin.readline()
    
    if input == '.\n':
        break

    n = input.replace(" ", "")

    for i in range(len(n)):
        if not stack:
            if n[i] == ')' or n[i] == ']':
                answer = "no"
                break

        if n[i] == '(' or n[i] == '[':
            stack.append(n[i])
        elif stack and n[i] == ')':
            if stack[-1] != '(':
                answer = "no"
                break
            else:
                stack.pop()
        elif stack and n[i] == ']':
            if stack[-1] != '[':
                answer = "no"
                break
            else:
                stack.pop()

    else:
        if not stack:
            answer = "yes"
        else:
            answer = "no"
        
    print(answer)