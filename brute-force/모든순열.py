from itertools import permutations
n = int(input())

for res in list(permutations(range(1,n+1),n)):
    print(*res)