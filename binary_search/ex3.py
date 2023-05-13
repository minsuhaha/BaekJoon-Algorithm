n, m = map(int,input().split()) # 떡의 개수 n, 요청한 길이 m
data = sorted(map(int,input().split())) # 오름차순으로 정렬
start = 0 # 시작점
end = max(data) # 맨 끝점
result = 0

while start <= end:
    total = 0 # 초기화
    mid = (start+end) // 2 # data의 중간지점의 값 구해주기 -> 이진탐색을 위해
    for d in data:
        if d > mid:
            total += d - mid
    if total < m: # 왼쪽 탐색
        end = mid - 1
    else: # 적어도 m보다는 커야하기 때문에 -> 오른쪽 탐색
        result = mid
        start = mid + 1

print(result)
    

    
