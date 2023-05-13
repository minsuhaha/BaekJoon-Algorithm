# 올바른 괄호인지 확인하는 것!
import sys
input = sys.stdin.readline
n = int(input())

lst = [list(input()) for _ in range(n)]

for i in range(n):
    count = 0
    if lst[i][0] == ')': # 시작은 ')'하면 정상적인 괄호가 아니므로 NO
        print("NO")
    else:
        for j in range(len(lst[i])):
            if count >= 0: # count가 -1로 가버리는 순간 if 문 밑으로 실행 안되도록!
                if lst[i][j] == '(':
                    count+=1
                elif lst[i][j] == ')':
                    count-=1
        if count == 0:
            print("YES")
        else:
            print("NO")
    
       