import sys
input = sys.stdin.readline
n = input().rstrip()
# 현재 코드는 str(num)에서 연속된 숫자가 나왔을 경우 상황을 고려 못함.
num = 0
idx = 0

while len(n) > idx:
    num += 1 
    for i in range(len(str(num))):
        if idx >= len(n):
            break
        if n[idx] == str(num)[i]:
            idx += 1
print(num)

    