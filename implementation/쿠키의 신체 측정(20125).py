# 머리 : 가장 먼저 나온 '*' 1칸
# 심장 : 머리 아래 1칸
# 허리 : 심장의 바로 아래 쪽 길이
# 왼쪽 팔 : 심장 기준 왼쪽 길이
# 오른쪽 팔 : 심장 기준 오른쪽 길이
# 왼쪽 다리 : 허리의 왼쪽 아래
# 오른쪽 다리 : 허리의 오른쪽 아래

import sys
input = sys.stdin.readline

n = int(input())
matrix = [input().rstrip() for _ in range(n)]

head, heart_x, heart_y, waist, left_arm, right_arm, left_leg, right_leg = 0, 0, 0, 0, 0, 0, 0, 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] == '*':
            # 머리 발견
            if not head:
                head = 1
                heart_x, heart_y = i+2, j+1
            
            # 팔 길이
            elif i+1 == heart_x:
                if j+1 < heart_y:
                    left_arm += 1
                elif j+1 > heart_y:
                    right_arm += 1

            # 허리 길이
            elif j+1 == heart_y and i+1 > heart_x:
                waist += 1

            # 다리 길이
            elif i+1 > heart_x:
                if j+1 == heart_y-1:
                    left_leg += 1
                elif j+1 == heart_y+1:
                    right_leg += 1

print(heart_x, heart_y)
print(left_arm, right_arm, waist, left_leg, right_leg)
