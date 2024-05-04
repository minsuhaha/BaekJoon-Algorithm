import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
location = list(map(int, input().split()))

result = []
if m == 1:
    print(max(location[0], n-location[0]))

else:
    for i in range(m):
        if i == 0:
            tmp = location[i+1] - location[i]
            if tmp % 2 == 0:
                height = max(location[i], tmp//2)
            else:
                height = max(location[i], tmp//2+1)

        elif i == m-1:
            height = n - location[i]
        
        else:
            tmp = location[i+1] - location[i]
            if tmp % 2 == 0:
                height = tmp//2
            else:
                height = tmp//2+1
        
        result.append(height) 
    print(max(result))
