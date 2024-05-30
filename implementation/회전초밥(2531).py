# 1번째 정답 코드

# import sys
# from collections import deque
# input = sys.stdin.readline

# n, d, k, c = map(int, input().split()) # n:초밥 개수, d:초밥 가짓수, k:연속해서 먹는 접시 수, c:쿠폰번호
# sushi = [int(input()) for _ in range(n)]

# max_count = len(set(sushi[:k]))
# left, right = 0, k-1
# start = 0

# while left < n:
#     sushi_count = len(set(sushi[left:right+1]))
#     if c not in sushi[left:right+1]:
#         sushi_count += 1
    
#     if sushi_count > max_count:
#         max_count = sushi_count
    
#     if right >= n-1:
#         sushi_switch = sushi[start]
#         sushi.append(sushi_switch)
#         start += 1
    
#     left += 1
#     right += 1

# print(max_count)

import sys
input = sys.stdin.readline


n, d, k, c = map(int, input().split()) # n:초밥 개수, d:초밥 가짓수, k:연속해서 먹는 접시 수, c:쿠폰번호
sushi = [int(input()) for _ in range(n)]
left, right = 0, k-1
max_count = 0
sushi_count = 0

while left < n:
    if left <= n-k:
        sushi_set = set(sushi[left:right+1])
    else:
        sushi_set = set(sushi[left:] + sushi[:right+1])

    if c not in sushi_set:
        sushi_count = len(sushi_set) + 1
    else:
        sushi_count = len(sushi_set)
        
    max_count = max(sushi_count, max_count)

    left += 1
    right = (right+1)%n

print(max_count)
    


