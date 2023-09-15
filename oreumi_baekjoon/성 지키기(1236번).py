n, m = map(int, input().split())

lst = [list(input()) for _ in range(n)]
row_cnt = 0
for i in range(n):
    if 'X' not in lst[i]:
        row_cnt += 1

col_cnt = 0
for i in range(m):
    cnt = n
    for j in range(n):
        if 'X' in lst[j][i]:
            break
        cnt -= 1
        
    if cnt == 0:
        col_cnt += 1

print(max(row_cnt, col_cnt))