import sys
input = sys.stdin.readline
n = int(input())
result = []
for _ in range(n):
    ps = input()
    count = 0 
    for p in ps:
        if count >= 0:
            if p == '(':
                count += 1
            elif p == ')':
                count -= 1
        else:
            break
    
    if count == 0:
        print('YES')
    else:
        print('NO')
