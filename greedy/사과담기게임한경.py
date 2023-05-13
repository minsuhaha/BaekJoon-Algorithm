num = int(input())
lst = sorted(map(int,input().split()))
# lst.sort
lst2 = []

# mini=0
if num % 2 == 0: 
# 짝수일 경우은 가장 큰것하고 작은것의 합들을 리스트에 담는다
    for i in range(num//2):
        mus = lst[i]+lst[-(i+1)]
        lst2.append(mus)
    # mini = max(lst2) #이후 max값을 M으로 둔다.
else: 
    lst2.append(lst[-1])
# 홀수일경우 가장 lst에서 가장 큰값을 lst2에 집어넣고 짝수일 경우와
# 유사하게 진행한다
    for i in range(num//2):
        mus = lst[i]+lst[-(i+2)] 
        lst2.append(mus)
    # mini = max(lst2)

print(max(lst2))