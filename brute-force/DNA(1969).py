'''
문제설명
    Hamming Distance란 길이가 같은 두 DNA가 있을 때, 각 위치의 뉴클오티드 문자가 다른 것의 개수이다. 
    만약에 “AGCAT"와 ”GGAAT"는 첫 번째 글자와 세 번째 글자가 다르므로 Hamming Distance는 2이다.

원하는 답
    우리가 할 일은 다음과 같다. N개의 길이 M인 DNA s1, s2, ..., sn가 주어져 있을 때 Hamming Distance의 합이 가장 작은 DNA s를 구하는 것이다. 
    즉, s와 s1의 Hamming Distance + s와 s2의 Hamming Distance + s와 s3의 Hamming Distance ... 의 합이 최소가 된다는 의미이다.
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dna = [input().rstrip() for _ in range(n)]
result = []

for i in range(m):
    dna_dict = {'A':0, 'C':0, 'G':0, 'T':0}
    for j in range(n):
        dna_dict[dna[j][i]] += 1

    max_value = max(dna_dict.values())
    max_dna = [key for key in dna_dict if dna_dict[key] == max_value]
    result.append(sorted(max_dna)[0])

cnt = 0
for i in range(n):
    for j in range(m):
        if result[j] != dna[i][j]:
            cnt += 1

print(''.join(result))
print(cnt)
