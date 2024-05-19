import sys
input = sys.stdin.readline

p, m = map(int, input().split()) # p : 플레이어 수, m : 방의 정원

rooms = [] # 전체 게임 방
for _ in range(p):
    l, n = input().split() # l : 레벨, n : 닉네임

    # 생성 된 방이 하나도 없다면 새로운 방 하나 생성해주기
    if not rooms:
        rooms.append([(int(l), n)])
        continue
    
    # 기존에 있는 입장 가능 한 방 들어가기
    enter = False
    for room in rooms:
        if len(room) < m and room[0][0] -10 <= int(l) <= room[0][0] + 10:
            room.append((int(l), n))
            enter = True
            break
        
    # 기존에 있는 방에 입장이 불가할 때 새로운 방 만들기
    if not enter:
        rooms.append([(int(l), n)])

for room in rooms:
    # 방에 정원이 찼는지 여부
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    
    # 방 마다 플레이어 닉네임 순으로 정렬
    room.sort(key=lambda x:x[1])

    for player in room:
        print(*player)
