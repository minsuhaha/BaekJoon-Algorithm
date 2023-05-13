# 재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.
# 0이 입력 받을 시 0전의 가장 최근 수 지우기 -> pop을 이용하면 되겠다
import sys
input = sys.stdin.readline
n = int(input())
stack = []
result = []

for i in range(n):
    stack.append(int(input()))
    if stack[-1] == 0:
        stack.pop() # 0 일단 pop 먼저해주고
        stack.pop() # 0 최근 수 pop
print(sum(stack))
    