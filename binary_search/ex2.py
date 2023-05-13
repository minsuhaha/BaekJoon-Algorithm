def binary_search(n_data, target, start, end): # 이진탐색 함수
    while start <= end:
        mid = (start+end) // 2 # 중간지점 뽑아내기
        if n_data[mid] == target: # target과 값이 일치하다면
            return mid  # while 빠져나오기
        elif n_data[mid] > target: # 범위 반으로 줄이기1
            end = mid - 1
        elif n_data[mid] < target: # 범위 반으로 줄이기2
            start = mid + 1
    return None # 없는 수일 경우 None 반환

n = int(input())
n_data = sorted(map(int, input().split()))
m = int(input())
target = sorted(map(int,input().split()))

for i in range(m):
    result = binary_search(n_data, target[i], 0, n-1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')