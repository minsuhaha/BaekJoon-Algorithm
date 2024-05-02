# Y : 2
# F : 3
# O : 4
import sys
input = sys.stdin.readline

n, game = input().split()

player = set(input().rstrip() for _ in range(int(n)))
player_cnt = len(player)

if game == 'Y':
    result = player_cnt
elif game == 'F':
    result = player_cnt // 2
else:
    result = player_cnt // 3

print(result)
