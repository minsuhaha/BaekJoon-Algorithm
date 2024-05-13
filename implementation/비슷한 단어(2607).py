import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
word1 = input().rstrip()
word1_counter = Counter(word1)

'''
비슷한 단어 (4가지 경우)
1. 같은 구성 (같은 종류의 문자가 같은 개수만큼 있을 경우)
2. 한 단어에서 한 문자를 바꾸면 같은 구성이 될 때

3. 한 단어에서 한 문자를 더하면 같은 구성이 될 때
4. 한 단어에서 한 문자를 제거하면 같은 구성이 될 때
'''
cnt = 0
for _ in range(n-1):
    word1_counter_copy = word1_counter.copy()
    word2 = input().rstrip()
    word2_counter = Counter(word2)
    wrong = {}

    # 예외처리
    if abs(len(word1) - len(word2)) >= 2:
        continue

    # 1. 같은 구성
    if word1_counter == word2_counter:
        cnt += 1

    # 2. 한 문자를 바꾸면 같은 구성이 될 때
    elif len(word1) == len(word2):
        wrong =  word2_counter - word1_counter_copy
    
    # 3. 한 문자를 더하면 같은 구성이 될 때
    elif len(word2) > len(word1):
        wrong = word2_counter - word1_counter_copy

    # 4. 한 문자를 빼면 같은 구성이 될 때
    elif len(word1) > len(word2):
        wrong = word1_counter_copy - word2_counter

    if len(wrong) == 1 and all(value < 2 for value in wrong.values()):
        cnt += 1

print(cnt)
