n = int(input())

score = list(map(int, input().split()))
new_score = []
max = max(score)
for s in score:
    new_score.append(s/max*100)

print(sum(new_score)/len(new_score))