word = input()

# 1. 재귀 함수를 사용하지 않고 문자열 뒤집기 방법을 통해서 팰린드롬 해결
# word의 길이가 짝수일 경우
if len(word) % 2 == 0:
    if word[:(len(word)//2)] == word[(len(word)-1):(len(word)//2-1) : -1]:
        print(1)
    else:
        print(0)
# word의 길이가 홀수일 경우
else:
    if word[:(len(word)//2)] == word[(len(word)-1):(len(word)//2) : -1]:
        print(1)
    else:
        print(0)

# # 2. 재귀함수를 사용하여 팰린드롬 해결
def palindrome(word):
    if len(word) <= 1:
        return 1
    # word의 첫글자와 word의 마지막 글자가 다를 때 팰린드롬이 아님
    elif word[0] != word[-1]:
        return 0
    # 맨 앞 맨 뒤 글자가 같기 때문에 잘라서 다시 재귀함수
    return palindrome(word[1:-1])

result = palindrome(word)
print(result)

# 3. for 문을 이용하여 해결
for i in range((len(word)//2)+1):
    if word[i] != word[-(i+1)]:
        break
if i == (len(word)//2):
    print(1)
else:
    print(0)