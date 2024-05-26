import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visitor = list(map(int, input().split()))

visit_cnt = sum(visitor[:x])
max_visit = visit_cnt
cnt = 1

# max_visit 값 찾기
for i in range(1, n-x+1):
    visit_cnt = visit_cnt - visitor[i-1] + visitor[x-1+i] # 윈도우 슬라이싱 -> sum을 계속해서 하는것보다 훨씬 효율적
    if visit_cnt > max_visit:
        max_visit = visit_cnt
        cnt = 1 # max visit 값이 변경됄때마다 cnt=1로 초기화
    elif visit_cnt == max_visit:
        cnt += 1

if max_visit == 0:
    print('SAD')
else:
    print(max_visit)
    print(cnt)
