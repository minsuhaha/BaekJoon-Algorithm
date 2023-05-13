n = int(input())
meet = []
for _ in range(n):
    start, end = map(int,input().split())
    meet.append((start, end))

meet = sorted(meet, key=lambda x:x[0])
meet = sorted(meet, key=lambda x:x[1])

prior_end = 0
count = 0

for first, end in meet:
    if prior_end <= first:
        count+=1
        prior_end = end

print(count)