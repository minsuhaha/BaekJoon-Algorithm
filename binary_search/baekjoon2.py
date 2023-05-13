n = int(input()) # 상근이가 가지고 있는 숫자개수
cards = sorted(map(int, input().split())) # 상근이가 가지고 있는 숫자
m = int(input()) # 비교할 숫자개수
checks = sorted(map(int, input().split())) # 상근이가 가지고 있는 숫자랑 같은지 비교

for check in checks:
    start = 0
    end = n-1
    result = False
    while (start <= end):
        mid = (start+end) // 2
        if check < cards[mid]:
            end = mid - 1
        elif check > cards[mid]:
            start = mid + 1
        else:
            result = True 
            break
    
    print(1 if result else 0, end =' ')
