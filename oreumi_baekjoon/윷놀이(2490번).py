for _ in range(3):
    games = input().split()
    cnt0 = 0
    cnt1 = 0
    for game in games:
        if game == '1':
            cnt1 += 1
        elif game == '0':
            cnt0 += 1
    if cnt1 == 4:
        print('E')
    elif cnt0 == 4:
        print('D')
    elif cnt0 == 3:
        print('C')
    elif cnt0 == 2:
        print('B')
    elif cnt0 == 1:
        print('A')