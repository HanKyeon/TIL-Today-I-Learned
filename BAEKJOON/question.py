
# 입력 및 그래프로 만들기
n = int(input())
d = []
for _ in range(n) :
    x = input()
    d.append(list(x))

# 인덱스 별 친구 목록. (간선 테이블)
fl = []
for a in d : # 테이블을 돌며 Y 인덱스 값들을 리스트로 받을 것
    fl.append(list(filter(lambda x: a[x] == "Y", range(len(a)))))

# dfs로 찾기. 친구목록 테이블, 친구 번호, 친구 확인 테이블, 횟수카운팅
def dfs(fl, v, cf, c) :
    c += 1 # 카운트를 위해 횟수 하나 증가
    cf[v] = 1 # 자기 자신 체크. 재귀 하기 위해 일단 자기 자신도.
    for i in fl[v] : # v번 사람의 친구 목록을 순회히면서
        if cf[i] != 1 and c < 3 : # 친구 체크 안되어있고, 카운트가 3 미만이면
            dfs(fl, i, cf, c) # 그 친구 친구를 찾기 위해 dfs 한 번 시킴.
            # c=1 자기 자신, c=2 1차 친구, c=3 2차친구. 따라서 c<3 조건
    return cf.count(1) # 친구 확인 테이블에서 친구로 판단한 1의 갯수 반환

mfn = 0 # 최대 친구수 초기화

for i in range(n) : # 친구들 다 dfs 할거다.
    check_friend = [0] * n # 친구 확인 테이블은 인덱스마다 초기화.
    nfn = dfs(fl, i, check_friend, 0) # dfs 호출. i번 인덱스 친구친구 수 반환 받음
    mfn = max(nfn, mfn) # 반복하며 반환된 친구 수와 기존 mfn 중 큰 수로 변경

print(mfn-1) # 자기 자신을 뺀 최대 친구친구 수 출력


# ========================

# 데이터 입력 받아 정리
n = int(input())
d = []
for _ in range(n) :
    x = input()
    d.append(list(x))
# 간선 데이터 테이블
friend_list = []
for a in d :
    friend_list.append(list(filter(lambda x: a[x] == "Y", range(len(a)))))
# dfs 사용. 2번만 하도록 c 추가.
def dfs(fl, idx, cf, c) :
    c += 1
    cf[idx] = 1
    for i in fl[idx] :
        if cf[i] != 1 and c < 3 :
            dfs(fl, i, cf, c)
    return cf.count(1)
# 최대 2친구 수 데이터
mfn = 0
# 0부터 n-1 친구 다 훑어서 최대 친구 수 비교하여 mfn에 최댓값 저장
for i in range(n) :
    check_friend = [0] * n
    nfn = dfs(friend_list, i, check_friend, 0)
    mfn = max(nfn, mfn)
# 자기자신도 친구로 쳤으므로 1 빼서 출력
print(mfn-1)
