import sys
input = sys.stdin.readline

s, p = map(int, input().split())
dna = list(input().rstrip())
check = dict(zip(['A', 'C', 'G', 'T'], map(int, input().split())))

ans = {'A':0, 'C':0, 'G':0, 'T':0}
cnt = 0

# dna 비밀번호 가능여부체크
def check_dict(ans):
    for key in ans:
        if ans[key] < check[key]:
            return 0
    return 1

# 초기 윈도우 설정
for d in dna[:p]:
    ans[d] += 1

# 초기 윈도우 설정 check_dict 함수 호출 후 cnt 값 반영
cnt += check_dict(ans)

for i in range(s-p):
    # 이전 start 지점 문자 -1
    ans[dna[i]] -= 1

    # end 지점 한칸 밀고 해당 문자 +1
    ans[dna[p+i]] +=1

    cnt += check_dict(ans)

print(cnt)
