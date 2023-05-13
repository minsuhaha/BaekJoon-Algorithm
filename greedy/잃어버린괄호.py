equation = input().split('-')
# '-' 기준으로 나눠서 배열만들어주기 -> 그래야 가장 최솟값을 만들수있음
# ex) 55 - 30 + 20 -> 55 - (30 + 20)

new = []
result = 0
for eq in equation:
    n =  list(map(int, eq.split('+')))
    new.append(sum(n)) # sum 메소드를 통해 매소드를 실행하면서 배열에서 한칸나오게 됨.


result = new[0] #맨앞부분은 무조건 '+' 이기 때문에 / 가장 앞부분과 가장 뒤부분은 숫자이기에 '-'불가
new = new[1:] # 이부분부터는 '-'로 간주
for n in new:
    result -= n
print(result)

#     for i in range(len(new)):
#         if len(new[i]) >= 2:
#             result-= sum(new[i])
#         result+=new[i]
# print(result)



