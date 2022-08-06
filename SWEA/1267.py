'''
작업순서

DFS의 기본을 알려주는 듯?
사이클이 없다.

입력
그래프의 정점 수 V 간선의 수 E
E개의 간선. 시작점 도착점 시 도 시 도 시 도 주어짐.

출력
#1 #2 #3 ... 
작업순서

#d[i] d[i+1]
'''
from collections import deque

# 위상정렬 함수
def t_sort(req, sten) :
    l = [] # 결과 담을거임
    # deque 사용. 먼저 처리된 것이 먼저 나와야 해서.
    q = deque()
    # require node가 없다면(reqn == 0) q에 추가
    for i in range(1, v+1) :
        if req[i] == 0 :
            q.append(i)
    # q 자료를 다 뺄 때까지 반복
    while q :
        x = q.popleft()
        l.append(x) # 결과 저장
        # 인덱스가 start지점, 도착지end 정보를 가진 staend의 x를 확인하여 그부분의 require nod를 줄임
        for i in sten[x] :
            req[i] -= 1
            if req[i] == 0 :
                q.append(i)
    # 결과를 반환
    return l

# testcase!!!!!!!!! testcase!!!!!!!!!!!!!! testcase!!!!!!!!!!!!
for testcase in range(1, 11) :
    # 입력
    v, e = map(int, input().split())
    d = list(map(int, input().split()))
    reqn = [0] * (v+1) # reqn[n] 하면 n번 노드의 요구되는 갯수 이렇게 쓰려고 v+1번
    staend = [[] for _ in range(v + 1)] # 이하동문
    # 노드의 정보를 한줄로 줬기에 range의 step을 2로 줘서 정보 저장
    for i in range(0, e * 2, 2) :
        reqn[d[i+1]] += 1
        staend[d[i]].append(d[i+1])
		# 출력
    print(f"#{testcase}", end=' ')
    for val in t_sort(reqn, staend) :
        print(val, end=' ')
    print()
