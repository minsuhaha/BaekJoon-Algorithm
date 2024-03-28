arr_n = list(map(int, input()))

for i in range(len(arr_n)):
    max_n = arr_n[i]
    idx = i
    for j in range(i+1, len(arr_n)):
        if arr_n[j] > max_n:
            max_n = arr_n[j]
            idx = j
    arr_n[i], arr_n[idx] = arr_n[idx], arr_n[i]

res = ''.join(map(str, arr_n))
print(res)


