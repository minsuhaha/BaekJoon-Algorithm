import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, k, t, m = map(int, input().split()) # n:팀 개수, k:문제개수, t:당신 팀 ID, m:로그개수
    score = {team:{} for team in range(1, n+1)} # 팀 별 점수(문제 별 점수도 있음)
    count_submit = {team:0 for team in range(1, n+1)} # 풀이 제출횟수
    last_submit = {team:0 for team in range(1, n+1)} # 마지막 풀이 시점

    for k in range(m):
        i, j, s = map(int, input().split())
        if j in score[i]:
            score[i][j] = max(s, score[i][j])
        else:
            score[i][j] = s
        count_submit[i] += 1 # 팀 답안 제출 횟수 증가
        last_submit[i] = k # 팀 별로 가장 마지막 제출했던 시점 저장

    total_score = {team:sum(score.values()) for team, score in score.items()}
    team_rank = sorted(total_score, key=lambda team:(-total_score[team], count_submit[team], last_submit[team]))
    result = team_rank.index(t)

    print(result+1)
