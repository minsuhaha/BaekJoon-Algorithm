n, new_score, p = map(int, input().split())

if n == 0:
    print(1)
else:
    scores = list(map(int, input().split())) 
    scores.append(new_score) # 일단 무작정 score 배열 뒤에 넣어주기
    scores.sort(reverse=True) # 내림차순으로 정렬해주기
    rank = scores.index(new_score) + 1
    if (n == p and (scores[-1] == new_score)) or (rank > p) :
    # n과p과 같을 때 new_score가 기존의 score배열에 있는 수보다 크지 않을때
    # rank가 p보다 커버릴때
        print(-1)
    else:
        print(rank)


# if n == 0: # n=0일경우 아무 score도 없는거니깐 무조건 1등
#     print(1)
# else:
#     scores = list(map(int,input().split())) # 내림차순으로 이미 score들이 주어짐

#     # 자기보다 스코어가 위에 있는 score 수가 곧 rank와 연결.
#     rank_dict = dict()  
    
#     if n >= p: # score가 꽉차있을때
#         # 스코어 위에 아무도 없을 경우도 rank=1 이기에 rank=1로 초기화
#         if new_score > scores[-1]: # scores배열은 내림차순으로 정렬되어 있기 때문에 가장 마지막 값이 최솟값임!
#         # 태수의 score가 scores배열에서의 가장 작은 값보다는 큰 수가 들어왔을때 -> 값 교체
#             scores[-1] = new_score
#         else:
#             print(-1)
#     else:
#         scores.append(new_score)
#     scores.sort(reverse=True)
#     for i in range(n):
#         rank = 1
#         for j in range(n):
#             if scores[i] < scores[j]:
#                 rank+=1
#         rank_dict[scores[i]] = rank

#     print(rank_dict[new_score])
    




        

