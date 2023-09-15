# 전부 대문자로 바꿔버림
words = input().upper()

# 첫번째 방법
# 중복 문자 제거
set_words = list(set(words))

lst = []
for word in set_words:
    lst.append(words.count(word))

# max 값이 두개 이상 일 경우
if lst.count(max(lst)) >= 2:
    print('?')
else:
    print(set_words[lst.index(max(lst))])


# 두번째 방법 dict 사용
count = dict()

for word in words:
    if word in count.keys(): # dict 안에 글자가 존재하면 개수 + 1
        count[word] += 1
    else: # dict 안에 글자가 존재하지 않을 경우 1로 초기화
        count[word] = 1

result = sorted(count.items(), key = lambda x : x[1], reverse = True)

max_value2 = 0
for idx, (k, v) in enumerate(result):
    if idx == 0:
        max_value1 = v  # 첫번째로 많이 등장한 글자 개수
        max_word = k   # 첫번째로 많은 글자 저장

    elif idx == 1:
        max_value2 = v  # 두번째로 많이 등장한 글자 개수
    
    elif idx == 2:
        break

if max_value1 == max_value2:  # max값이 같은 글자가 존재한다면
    print('?')
else: 
    print(max_word)