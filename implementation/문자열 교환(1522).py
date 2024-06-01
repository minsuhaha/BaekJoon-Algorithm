import sys
input = sys.stdin.readline
string = input().rstrip()

a_cnt = string.count('a') # a 개수 카운트

left, right = 0, a_cnt
string_cnt = len(string)
res = string_cnt # 교환 최소횟수 (b로만 구성되어있는 경우부터 시작)


while left < string_cnt:
    if right < string_cnt:
        r_string = string[left:right]
    else:
        r_string = string[left:] + string[:right-string_cnt]
    
    res = min(r_string.count('b'), res)

    # 슬라이싱 윈도우 (1칸씩 이동)
    left += 1
    right += 1

print(res)
