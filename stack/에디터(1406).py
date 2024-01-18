import sys
input = sys.stdin.readline

left = list(input().rstrip()) # 왼쪽 스택 : 초기 커서가 문자열 맨 끝에 있기에 입력값 전부 담기
right = [] # 오른쪽 스택

n = len(left) # 초기 입력받은 문자열 길이
m = int(input()) # 명령어 횟수
cursor = len(left)+1 # 초기 커서는 문자열 맨 끝에 있음

for _ in range(m):
    command = list(input().split())
    if command[0] == 'L' and cursor != 1: # 커서가 문장의 맨 앞이 아닐때만 작동
        cursor -= 1 # 커서를 왼쪽으로 한 칸 옮김
        right.append(left.pop()) # 왼쪽 스택에서 pop 한 문자 추가
    
    elif command[0] == 'D' and cursor != n+1: # 커서가 문장의 맨 뒤가 아닐 경우
        cursor += 1 # 커서를 오른쪽으로 한 칸 옮김
        left.append(right.pop()) # 왼쪽 스택에서 pop 한 문자 추가

    elif command[0] == 'B' and cursor != 1:
        cursor -= 1 # 문자가 하나 없어지기에 커서 값도 -1
        left.pop() # 왼쪽 스택 top 문자 pop
        n -= 1 # 전체 문자열 길이에서 -1
    
    elif command[0] == 'P':
        left.append(command[1])
        cursor += 1 
        n += 1
    
ans = ''.join(left + right[::-1]) # 왼쪽, 오른쪽 스택 합치고 문자열로 변환
print(ans)

