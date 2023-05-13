n, m = map(int,input().split())

listen = set()
see = set()

for i in range(n):
    listen.add(input())

for i in range(m):
    see.add(input())

result = list(listen&see)
result.sort()

print(len(result))
for i in range(len(result)):
    print(result[i])


