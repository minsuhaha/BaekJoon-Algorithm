n = int(input())
m = int(input())

# 서로 연결되어있는 graph 리스트 만들어주기 (해당 번호의 컴퓨터에 어떠한 컴퓨터들이 연결되어 있는지 파악)
# 1 ~ 7 번 컴퓨터 각각 연결되어있는 컴퓨터들 번호 넣어주기
graphs = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    # graph 양방향 연결되어있는것을 표시 (1,2) 이면 graphs에서 컴퓨터1에도 2넣어주고 컴퓨터2에도 1넣어주고
    graphs[a].append(b)
    graphs[b].append(a)

# 서로 연결되어있는지 파악하기 위해 visited 변수생성
visited = [0]*(n+1)
def dfs(num):
    visited[num] = 1
    for graph in graphs[num]:
        if visited[graph] == 1:
            continue
        dfs(graph)
    
# 컴퓨터 1과 연결되어있는 컴퓨터들을 파악해야 되기에 초기값 1을 넣어줌
dfs(1)
# 컴퓨터 1에 값은 빼줘야 하기에
print(sum(visited) - 1)
    
