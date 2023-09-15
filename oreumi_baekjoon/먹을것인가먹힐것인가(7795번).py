T = int(input())

def binary(target, B):
    start = 0
    end = len(B) - 1
    while start <= end:
        mid = (start+end) // 2
        
        # B[mid] == target 일 경우는 target이 더 큰 숫자가 아니므로 포함하지않는다.
        if B[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    # 마지막 start는 target 보다 앞에있는 인덱스 개수를 나타내줌      
    return start


for _ in range(T):
    n, m = map(int, input().split())
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))
    
    result = 0
    for a in A:
        result += binary(a, B)
    print(result)


    # cnt = 0
    # for a in A:
    #     for b in B:
    #         if a <= b:
    #             break
    #         cnt += 1
    
    # print(cnt)
