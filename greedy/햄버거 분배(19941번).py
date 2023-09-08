import sys
input = sys.stdin.readline

n, k = map(int, input().split())
eat = list(input().rstrip())

cnt = 0
for i in range(n):

    # 사람이면
    if eat[i] == 'P':
        # 사람 앞뒤로 k만큼 탐색
        for j in range(i-k, i+k+1):
            # j의 가능범위 지정
            if 0 <= j <= n-1: 
                if eat[j] == 'H': # 햄버거를 발견한 첫 순간
                    cnt += 1
                    eat[j] = 'D' # 한명의 사람이 햄버거를 이미 먹었다 표시
                    break # 한명의 사람이 먹을 수 있는 햄버거는 한개이여야 더 많은 사람들이 햄버거를 먹을 수 있기에
print(cnt)