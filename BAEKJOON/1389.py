'''
먹음직스러운 베이컨의 6단계 법칙

지구촌은 6다리 건너면 다 아는 사이다. 케빈 베이컨 게임은 임의의 두 사람이 최소 몇 단계만에 이어질 수 있는지 계산하는 게임.

입력
첫째줄에 유저 수 2이상 100이하 n, 친구 관계 수 1이상 5000이하 m.
m개의 친구 관계. A B는 친구 B A도 친구. 노친구 없음. 모든 사람은 연결되어 잇음.
'''
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
fl = [set() for _ in range(n+1)] # 중복친구 대비용 set로 만들어줌
for i in range(m):
    a, b = map(int, input().rstrip().split())
    fl[a].add(b)
    fl[b].add(a)

bsum = int(10e9) # 최소합
ans = 0 # 정답
for i in range(1, n+1): # 1부터 n번 사람까지 순회
    v = [-1]*(n+1) # 방문
    q = deque() # 큐
    q.append((i, 0)) # i, 0
    v[i] = 0 # 자기 자신 처리
    ret = 0 # 리턴값인데 번호의 친구 합
    b = bsum # 최솟값이 갱신 되면 ans를 갱신하기 위한 이전 최솟값 저장
    while q: # 큐가 빌 때까지
        num, c = q.popleft() # 숫자랑 거리
        ret += c # 리턴값에 거리 더해줌
        if ret >= bsum: # 리턴값이 현 최솟값보다 커지면 break
            break
        for j in fl[num]: # 친구 리스트 순회
            if v[j] == -1: # 방문 안했으면
                v[j] = c+1 # 거리로 방문해주고 -> 거리로 방문 할 이유 없긴 함.
                q.append((j, c+1)) # 큐에 추가
    bsum = min(bsum, ret) # 최솟값 갱신 해봤는데
    if b != bsum: # 바뀌면
        ans = i # 정답에 저장
print(ans) # 출력

