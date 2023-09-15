N, M = map(int, input().split())
DNA = [list(input()) for _ in range(N)]

lst = ['A', 'C', 'G', 'T'] # 사전순으로 lst 담아주기
result = ''
count = 0
for i in range(M):
    cnt = [0] * 4 # lst 길이만큼
    for j in range(N):
        if DNA[j][i] == 'A':
            cnt[0] += 1
        elif DNA[j][i] == 'C':
            cnt[1] += 1
        elif DNA[j][i] == 'G':
            cnt[2] += 1
        elif DNA[j][i] == 'T':
            cnt[3] += 1
    
    result += lst[cnt.index(max(cnt))]
    count += N - max(cnt)

print(result)
print(count)
        