# 입력으로 숫자가 들어왔다면 그 숫자에 해당하는 포켓몬의 이름을, 문자가 들어왔으면 그 포켓몬의 이름에 해당하는 번호를 출력
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dict_name_first = {}
dict_num_first = {}

for i in range(n):
    # 한줄씩 입력받을때에는 공백문자를 제거해주기 위해 rstrip()를 뒤에 꼭 붙여주기 
    name = input().rstrip()
    dict_name_first[name] = i+1
    dict_num_first[i+1] = name

for i in range(m):
    k = input().rstrip()
    if k.isalpha():
        print(dict_name_first[k])
    else:
        print(dict_num_first[int(k)])



