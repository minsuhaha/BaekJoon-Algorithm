x = int(input())
dp = [0]*(x+1) # 1 ~ x까지 리스트 초기화

# 보텀업(상향식 방식 사용) : 밑에서부터 위로
for i in range(2, x+1): # 2부터 시작, 1은 0번의 연산이기에 포함 x
    dp[i] = dp[i-1] + 1 # 빼기 1을 했을 경우 / +1은 연산횟수라 포함해줘야함!
    # dp[i - 1]은 이미 최적값으로 저장되어 있다는 걸 꼭 기억해주기    

    # min()함수를 시용해서 더 작은 연산횟수 값을 dp[i]에 넣어주기
    # elif을 사용하면 하나만 비교하고 끝나기 때문에 전부 비교를 해주기 위해서 if문으로만 구성
    if dp[i] % 5 == 0:
        dp[i] = min(dp[i], dp[i//5]+1)
    if dp[i] % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if dp[i] % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[x])


