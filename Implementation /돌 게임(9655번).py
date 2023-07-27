N = int(input())
# N이 홀수면 상근이가 이기고, 짝수면 창영이가 이긴다?
result = 'CY' if N % 2 == 0 else 'SK'
print(result)