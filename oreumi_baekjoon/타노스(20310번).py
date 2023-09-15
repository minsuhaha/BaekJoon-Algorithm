s = input()

# s 문자열에 '1'의 빈도수의 절반만 앞에서 부터 제거하기
new_s = s.replace('1','',s.count('1')//2)

# 뒤집기
new_s = new_s[::-1]

# s 문자열에 '0'의 빈도수의 절반만 앞에서 부터 제거하기
new_s = new_s.replace('0', '', s.count('0')//2)

# 원래대로 다시 뒤집기
new_s = new_s[::-1]

print(new_s)