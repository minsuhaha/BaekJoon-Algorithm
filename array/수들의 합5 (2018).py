n = int(input())

start = 1
end = 1
sum = 1
cnt = 1 # 숫자 하나로는 무조건 표현 할 수 있기 때문에 초기화를 1로.

while end!=n:
    if sum == n:
        cnt += 1
        end += 1
        sum += end
    elif sum < n:
        end += 1
        sum += end
    elif sum > n:
        sum -= start
        start+=1

print(cnt)
