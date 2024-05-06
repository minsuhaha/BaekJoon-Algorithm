import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    teams = list(input().split())

    teams_count = Counter(teams)
    re_teams = [team for team in teams if teams_count[team] == 6]

    teams_score = {}
    for score, team in enumerate(re_teams):
        if teams_count[team] > 2:
            if team not in teams_score:
                teams_score[team] = score+1
                teams_count[team] -= 1
            else:
                teams_score[team] += score+1
                teams_count[team] -= 1
    
    min_score = min(teams_score.values())
    min_teams = [team for team, score in teams_score.items() if score == min_score]

    if len(min_teams) == 1:
        print(min_teams[0])
    else:
        min_teams_count = {team : 0 for team in min_teams}
        for team in re_teams:
            if team in min_teams_count:
                min_teams_count[team] += 1
                if min_teams_count[team] > 4:
                    print(team)
                    break
