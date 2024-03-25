n = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)
avg = 0

for score in scores:
    avg += score/max_score * 100

print(avg/n)
