# 4
# 123 1 1
# 356 1 0
# 327 2 0
# 489 0 1

# Permutation(순열) -> 중복허용 (1,2,3) (3,2,1) -> 자리수가 중요한 숫자야구게임에서는 둘다 파악해야 되기에 순열을 사용!
# 무조건 영수 입장에서 생각하기!
import copy
import sys
from itertools import permutations
input = sys.stdin.readline

num = list(range(1,10))
num = list(permutations(num, 3))

n = int(input())

for _ in range(n):
    pred, s, b  = map(int,input().split())
    pred = list(str(pred)) # 숫자 하나하나싹 바교해주기 위해 -> str : '123' -> list : ['1','2','3']
    minus = 0

    for i in range(len(num)): # 모든 경우의 수의 길이 만큼 for 돌려줌 -> 완탐의 기본 : 모두 다 탐색 
        s_count = 0
        b_count = 0
        i -= minus        

        for j in range(3): # 3자리 수밖에 없기에
            if int(pred[j]) in num[i]: # 일단 num[i]안에 있는거니깐 자리수가 같으면 strike +1, 자리수는 다르면 ball +1
                if int(pred[j]) == num[i][j]: # 자리수 마저 같으면
                    s_count+=1
                else: # 자리수는 다르면
                    b_count+=1
       
        if s_count != s or b_count != b:
            num.remove(num[i])
            minus += 1

print(len(num))


        # if (s_count != s) or (b_count != b):
        #     num.remove(num[i]) # 해당 num은 영수가 생각하는 경우의 수에 포함 되지 않는다
        #     minus += 1 # num을 하나 삭제했기 때문에 list out of index가 뜨지 않으려면 i에서 -1 해줘야 하기 때문에 설정


            
            
    

