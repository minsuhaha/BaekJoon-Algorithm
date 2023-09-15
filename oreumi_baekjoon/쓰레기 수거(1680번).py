T = int(input()) # 테스트 케이스 수

for _ in range(T):
    # W : 쓰레기차의 용량, N : 지점의 개수
    W, N = map(int, input().split()) 
    
    weight = 0 # 현재 쓰레기 차의 용량
    dist = 0 # 누적 거리
    pre_dist = 0 # 현재 바로 이전의 거리
    
    for i in range(N):
        x, w = map(int, input().split()) # x : 쓰레기장으로부터의 거리, w : 해당 지점의 쓰레기 양
        # 현재 쓰레기 차의 용량 + 해당 지점 쓰레기 양이  < 쓰레기 차의 용량보다 작다면
        if weight + w < W:
            weight += w # 현재 쓰레기 차 용량에 해당 지점 쓰레기를 담아주기
            dist += (x - pre_dist) # 현재 쓰레기 차가 움직인 거리를 dist에 누적해서 더해주기

            if i == N-1: # 쓰레기 지점 마지막 부분이라면 다시 쓰레기 장으로 돌아가야되니 + x
                dist += x

        # 현재 쓰레기 차의 용량 + 해당 지점 쓰레기 양 == 총 쓰레기 차의 용량
        elif weight + w == W:
            weight = 0 # 현재 쓰레기 차의 용량 비워주기 -> 쉽게 쓰레기 장을 돌아가서 쓰레기를 뺀다라고 생각하면 될듯!
            dist += (x-pre_dist) + x*2    # x*2 를 더해주는 이유는 해당 지점에서 쓰레기 장으로 가서 쓰레기 빼고 다시 돌아온다 라는 의미!
        
            if i == N-1: # 쓰레기 지점 마지막 부분이라면
                dist -= x

        elif weight + w > W:
            weight = 0 # 다시 쓰레기 장으로 가서 현재 쓰레기 차의 용량 비워주기
            dist += (x-pre_dist) + x*2

            if i == N-1: # 쓰레기 지점 마지막 부분이라면
                dist += x

        pre_dist = x  # pre_dist를 현재 지점으로 바꾸기
        
    print(dist)

    
    


