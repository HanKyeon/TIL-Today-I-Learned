'''
음료수 얼려먹기
n*m 칸에 얼린다.
1은 얼음이 껴있고 0은 음료수 (구멍이 뚫린 부분은 0, 얼음이 언 부분은 1)
이어진 부분끼리 아이스크림 1개.
총 아이스크림 갯수는?

ex)
3 3
001
010
101

-> 3개.

0으로 이뤄진 부분들이 몇개인지 확인 하는 것.
n, m은 1이상 1000 이하의 수.

'''
# n, m 입력 받기
n, m = map(int, input().split())
# 그래프를 빈 배열로 만듬
graph = []
# 일렬로 입력받은 수를 각각 int 처리하며 리스트로 만들어 넣음.
# [x][y]가 좌표가 되도록 만들어진다.
for i in range(n) :
    graph.append(list(map(int, input())))
# dfs 함수
def dfs(x, y) :
    # 일단, 훑는 것이 영역을 벗어나면 실행하지 않는다.
    # x값, 행은 0~n-1까지의 index를 가지고
    # y값, 열은 0부터 m-1의 index를 가지기에
    # 해당 영역이 아니라면 false를 반환한다.
    if x <= -1 or x>= n or y <= -1 or y >= m :
        return False
    # 만약 x, y가 방문하지 않았다면
    if graph[x][y] == 0 :
        graph[x][y] = 1 # 방문처리 하고
        dfs(x - 1, y) # 위쪽
        dfs(x, y - 1) # 왼쪽
        dfs(x + 1, y) # 아래쪽
        dfs(x, y + 1) # 오른쪽
        return True #재귀 돌려서 방문처리 하고 True 반환해라.

    return False # 재귀 함수의 리턴은 False 이다.
# 갯수 초기화
result = 0
# i, j행렬 모두 훑는다 0,0 부터 dfs 시작한다.
for i in range(n) :
    for j in range(m) :
        # 재귀함수이므로 방문하지 않은 곳부터 시작해서 DFS로 인접한 곳을
        # 싹 훑는다. 0을 만나면 훑기 시작해서 주변 0을 다 훑고 True를 반환
        # 하므로 True가 나올 때마다 1개가 추가되어야 한다.
        if dfs(i, j) == True : 
            result += 1


