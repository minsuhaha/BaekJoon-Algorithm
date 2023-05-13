import sys
input = sys.stdin.readline

data = input()
stack = []
count = 0

for i in range(len(data)):
    if data[i] == '(':
        stack.append(data[i])
    elif data[i] == ')':  # ')' 일 경우 무조건 pop 해줌
        stack.pop()
        if data[i-1] == '(': # 레이저인 경우
            count += len(stack)
        else: # 레이저가 아닐 경우
            count += 1

print(count)
