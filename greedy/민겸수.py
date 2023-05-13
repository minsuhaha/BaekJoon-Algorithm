data = input()

m = 0
min = ''
max = ''

for dat in data:
    if dat == 'M':
        m += 1 # m몇개나왔는지 count -> m이 나왔다고 바로 값을 매길 수 없기에 count해주기
    elif dat == 'K':
        if m == 0: # 앞에 m이 없었을때
            max += '5'
            min += '5'
        else:
            max += '5'+'0'*m
            min += '1'*1+'0'*(m-1)+'5'
            m = 0 # m다시 0으로 초기화

if m != 0: #마지막에 M이 연달아 등장했을때 / 마지막이 K가 나왔다면 m이 0일때나 0으로 만들어주거나 이기에 해당 안됨
    max += '1'*m # -> 마지막 m이기에 k가 따로 나오지않기에 1111식으로 변환해주기 1000보다는 크니깐
    min += '1'*1+'0'*(m-1)

print(max)
print(min)



