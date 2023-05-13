import sys
input = sys.stdin.readline
n, new_score, p  = map(int, input().split())


if n == 0:
    print(1)
else:
    scores = list(map(int, input().split()))
    if n == p: # n이 꽉차있을 경우
        if scores[-1] >= new_score:
            print(-1)
        else:
            scores.append(new_score)
            scores.sort(reverse=True)
            rank = scores.index(new_score)
            print(rank+1)
    else:
        scores.append(new_score)
        scores.sort(reverse=True)
        rank = scores.index(new_score)
        print(rank+1)
