import sys
input = sys.stdin.readline
n, m = map(int, input().split())
weather = [list(input().rstrip('\n')) for _ in range(n)]
# input().rstrip()을 사용해주므로써 '\n'제거

result = [[0]*m for _ in range(n)]

for i in range(n):
    cloud=False
    for j in range(m): 
        if weather[i][j] == 'c': # 구름이 있다면 구름은 동쪽 즉 오른쪽으로만 이동함.
            result[i][j] = 0
            cloud = True # 해당 행에 구름이 있었다를 기록해주기위해 -> True
            count = 1 # 구름 오른쪽 다음은 구름을 다시 만나기 전까지 1부터 숫자 시작

        elif weather[i][j] == '.' and cloud == True:
            result[i][j] = count
            count+=1 # count 1개 더 늘려주기
        
        elif weather[i][j] == '.' and cloud == False:
            result[i][j] = -1

for res in result:
    print(*res)
