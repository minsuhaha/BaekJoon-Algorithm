import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
nums = list(permutations(range(1, 10), 3))

for _ in range(n):
    pred_num, s, b = map(int, input().split()) 
    pred_num = list(str(pred_num))

    for num in permutations(range(1, 10), 3):
        s_cnt = 0
        b_cnt = 0
        if num in nums:
            for i in range(3):
                if str(num[i]) == pred_num[i]:
                    s_cnt += 1
                elif str(num[i]) in pred_num:
                    b_cnt += 1
        
            if s != s_cnt or b != b_cnt:
                nums.remove(num)

print(len(nums))
