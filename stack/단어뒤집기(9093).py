import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    words = list(input().split())
    result = []
    for word in words:
        re_word = word[::-1]
        result.append(re_word)
    answer = ' '.join(result)
    print(answer)
