import sys
input = sys.stdin.readline
n, m = map(int, input().split())

words = {}
for i in range(n):
    word = input().rstrip()
    
    if len(word) < m:
        continue
    elif word in words:
        words[word] += 1
    else:
        words[word] = 1

# 1. 빈도수, 2. 단어 길이, 3. 알파벳 순서
word_list = sorted(words.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

for word in word_list:
    print(word[0])


