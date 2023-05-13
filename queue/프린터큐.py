# 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.

# 문서의 개수 N(1 ≤ N ≤ 100)과
# 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M
# 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 
# 중요도가 같은 문서가 여러 개 있을 수도 있다.

# 입력예시
# 3
# 1 0 -> 현재 큐에서 0번째에 놓여있는 정수M이 몇번째로 출력되냐?
# 5 -> 중요도 -> 결과 : 1번째 출력

# 4 2 -> 현재 큐에서 2번째에 놓여있는 정수 M이 몇번째로 출력되냐?
# 1 2 3 4 -> '3'이 몇번째로 출력되는지 물어보는것 -> 2번째로 출력

# 6 0 -> 0번째에 놓여있는 정수M이 몇번째로 출력되냐?
# 1 1 9 1 1 1 -> 5번째로 출력!

# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
# 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다. -> KeyPoint
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split())) # [1, 2, 3, ]
    idx = deque(i for i in range(n)) # 몇번째 위치인지 파악하기 위한 idx 배열 생성 / 0번째부터 시작
    # idx = [0, 1, 2, ]
    rank = 0
    while queue:
        if queue[0] == max(queue): # queue의 가장 앞에 있는 값이 max값이면 rank = 1 -> 다음 max는 rank=2
            rank+=1 
            queue.popleft() # 가장 처음에 있는 값 빼주기
            if idx.popleft() == m: # 몇번째 값을 구하려고 하는지 파악     
                print(rank) # idx배열에 순서와 구하려고 하는 순서가 같다면 rank가 몇인지 출력
        else:
            # queue랑 idx랑 같이 움직이기
            queue.append(queue.popleft())
            idx.append(idx.popleft())
    # 모든 idx 위치에 rank값을 구해줄 필요없다. 문제에서 필요한 m번째 위치 rank만 출력           

