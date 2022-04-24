import sys
input = sys.stdin.readline

s = input()

if '{' in s or '}' in s:
    print(0)
    exit(0)

if s[0] == ']' or s[0] == ')':
    print(0)
    exit(0)

stack = []
for i in range(len(s)):
    print(stack, i)
    if s[i] == '(' or s[i] == '[':
        stack.append(s[i])
    else:
        if s[i] == ')': # 끝이 ) 인 경우
            if len(stack) > 0:
                if stack[-1] == '(': # 스택 끝이 ( 인 경우
                    stack[-1] = 2
                elif stack[-1] == '[': # 이상한 경우에 탈출~!~!
                    print(0)
                    exit(0)
                else: # 스택의 끝이 ( 이 아니라, 숫자
                    temp = 0
                    for j in range(len(stack) - 1, -1, -1):
                        if stack[j] == '(':
                            stack[-1] = int(temp * 2)
                            break
                        elif stack[j] == '[':
                            print(0)
                            exit(0)
                        else:
                            temp += int(stack[-1])
                            stack.pop()
            else: 
                print(0)
                exit(0)
        if s[i] == ']' and stack:
            if len(stack) > 0:
                if stack[-1] == '[':
                    stack[-1] = 3
                elif stack[-1] == '(':
                    print(0)
                    exit(0)
                else:
                    temp = 0
                    for j in range(len(stack) - 1, -1, -1):
                        if stack[j] == '[':
                            stack[-1] = int(temp * 3)
                            break
                        elif stack[j] == '(':
                            print(0)
                            exit(0) 
                        else:
                            temp += int(stack[-1])
                            stack.pop()

if '(' in stack or '[' in stack or ')' in stack or ']' in stack:
    print(0)
else:
    print(sum(stack))