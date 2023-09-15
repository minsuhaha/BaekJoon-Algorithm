# 한 단어에서는 여러 UCPC중의 단어가 속할수있음!!

# 공백을 제거
words  = input().replace(' ','')

find_word = 'UCPC'
idx = 0
for word in words:
    if find_word[idx] in word:
        idx += 1
    if idx == 4:
        break
        
if idx == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')