n, x = map(int, input().split())

visit = list(map(int, input().split()))

result = []

for i in range(n):
    total = visit[i]

    for j in range(i+1, i+x):
        if j > n-1:
            break
        total += visit[j]

    result.append(total)

max_visit = max(result)
if max_visit == 0:
    print('SAD')
else:
    print(max(result))
    print(result.count(max(result)))