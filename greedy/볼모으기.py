n = int(input())
colors = input()
# colors = [color for color in colors]
# RBBBRB /RRR

    
color1 = colors.rstrip("R")
color1 = color1.count("R")

color2 = colors.lstrip("R")
color2 = color2.count("R")

color3 = colors.rstrip("B")
color3 = color3.count("B")

color4 = colors.lstrip("B")
color4 = color4.count("B")

print(min(color1, color2, color3, color4))

# # 빨강 블루를 한쪽으로 몰아야함. 

# # 빨강색 오른쪽 밀기
# count1 = 0 # 움직이는 수
# total1 = 0 # 총 움직이는 수
# for i in range(n):
#     if colors[i]                                                                          == 'R':
#         count1+=1
#     elif colors[i] == 'B':
#         total1 += count1
#         count1 = 0
        
# # 빨강색 왼쪽 밀기
# count2 = 0
# total2 = 0
# colors.reverse()
# for i in range(n):
#     if colors[i] == 'R':
#         count2+=1
#     elif colors[i] == 'B':
#         total2 += count2
#         count2 = 0

# # 블루 오른쪽으로 밀기
# count3 = 0
# total3 = 0
# for i in range(n):
#     if colors[i] == 'B':
#         count3+=1
#     elif colors[i] == 'R':
#         total3 += count3
#         count3 = 0

# # 빨강색 왼쪽 밀기
# count4 = 0
# total4 = 0
# colors.reverse()
# for i in range(n):
#     if colors[i] == 'B':
#         count4+=1
#     elif colors[i] == 'R':
#         total4 += count4
#         count4 = 0

# print(min(total1,total2,total3,total4))
