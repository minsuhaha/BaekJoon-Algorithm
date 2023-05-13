n = int(input())
data = list(map(int, input().split()))
m = int(input())

start = 0
end = max(data)

while start <= end:
    total = 0 # 총액
    mid = (start+end) // 2 # 에상 상한액
    for d in data: 
        total += min(d,mid)
    if total > m:
        end = mid - 1
    else:
        start = mid + 1
print(end)