m = int(input())
n = int(input())

lst = []
for num in range(m, n+1):
    if num == int(num**0.5) ** 2:
        lst.append(num)

if len(lst) > 0:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)