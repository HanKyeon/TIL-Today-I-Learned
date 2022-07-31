'''
친구친구
인원 N
'''
'''
DFS 사용하기 적합한 예제는 아니다.
이미 방문했다면 재방문 하지 않는데
깊이 우선이라서 꼬일 수가 있다.
예를 들어, 1번 노드가 2,3번과 친구이고
2번 노드가 3번 노드와 친구
3번 노드가 4,5,6번 노드와 친구라면
2번 노드를 DFS 하면서 3번 노드를 방문처리가 되어버려서
1번 노드와 인접한 3번 노드에 대한 DFS가 이뤄지지 않는다.
'''
# 입력 및 그래프로 만들기
n = int(input())
d = []
for _ in range(n) :
    d.append(list(input()))

# 인덱스 별 친구 목록
fl = [] # 인덱스 별 친구 목록을 2차원으로 생성
for a in d :
    fl.append(list(filter(lambda x: a[x] == "Y", range(len(a)))))

# dfs로 찾기. 친구목록 테이블, 친구 번호, 친구 여부 확인, 횟수제한
def dfs(idx, c) :
    if c >= 3 :
        return
    
    check_friend[idx] = 1
    for i in fl[idx] :
        if c < 3 :
            dfs(i, c+1) # 반복.
    return check_friend.count(1) # 친구 확인 목록에서 1의 갯수 반환

mfn = 0 # 비교용 최대 친구수 초기화

# check_friend = [0] * n
# dfs(4, 0)

for i in range(n) : # 친구들 다 훑는다.
    check_friend = [0] * n # 친구 여부를 그때그때 초기화 해야함.
    nfn = dfs(i, 0) # dfs 호출.
    mfn = max(mfn, nfn) # dfs 반환된 친구 수와 기존 mfn 중 큰 수로 변경

print(mfn-1) # 자기 자신을 뺀 최대 친구 수 출력


