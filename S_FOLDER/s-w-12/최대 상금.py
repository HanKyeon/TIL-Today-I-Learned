'''
최대 상금

입력
전체 테케 수
숫자판, 교환 횟수 제시.
정수형, 최대 자릿수는 6자리, 최대 교환 횟수 10번.

출력
#테케 최대 금액
'''
'''
- 아이디어

1. 홀수번째 끼리 반복되는 경우, 짝수번째 끼리 반복되는 경우를 없애면 될 것이라 판단.

2. 홀-홀 은 2번 반복되어 겹치므로 제거해야 함. 짝-짝도 마찬가지.

3. 따라서 깊이를 정해주고, dep % 2와 리스트를 set에 함께 넣어주어 홀수일 때 짝수일 때 같은 수여도 다른 수임을 체크해야 함. 리스트와 홀짝 여부를 함께 들어야 하므로 set 사용.
3-1. set에 넣을 때 튜플 안의 list도 튜플로 만들어야 해시에러가 안남.

4. n이 되기 전까지 홀, 짝으로 가능한 모든 경우를 넣어주며, n % 2와 dep % 2가 같다면 ans에 기록.
4-1. n 이전 최댓값이 나오는 경우라면 같은 자리 두 번 바꾸면 같아지므로.(2번 내용) 이후 dep%2에서 반복에 들어 갈 이유가 없음.

5. 크게 본다면 DFS/BFS로 진행한다. 전부 확인하는데, 홀/짝일 때 방문 처리를 따로 해주는.
'''
# DFS 백트래킹

def 함수(li, dep):
    global ans, n
    vcal = [li[i]*tenten[i] for i in range(lnl)]
    if dep%2 == n%2:
        if ans < sum(vcal):
            ans = sum(vcal)
    if dep == n:
        return
    for i, j in combi:
        li[i], li[j] = li[j], li[i]
        if (tuple(li), (dep+1)%2) not in sets:
            sets.add((tuple(li), (dep+1)%2))
            함수(li, dep+1)
        li[i], li[j] = li[j], li[i]

for tc in range(1, int(input())+1):
    nl, n = input().rstrip().split() # 입
    nl, n = list(map(int, list(nl))), int(n) # 력
    lnl = len(nl) # 자주쓰길래 변수화
    sets = set() # 중복처리용.
    combi = []
    for i in range(lnl-1):
        for j in range(i+1, lnl):
            combi.append((i, j))
    ans = 0
    tenten = [10**(lnl-i-1) for i in range(lnl)]
    sets.add((tuple(nl), 0))
    함수(nl, 0)
    print(f"#{tc} {ans}")


# BFS
from collections import deque

def 큐사용():
    global n
    tenten = [10**(len(nl)-i-1) for i in range(len(nl))]
    combi = [] # 갈 수 있는 경우의 수
    for i in range(len(nl)-1):
        for j in range(i+1, len(nl)):
            combi.append((i, j))
    sets = set() # 중복처리용.
    ret = 0
    sets.add((tuple(nl), 0))
    q = deque()
    q.append((nl, 0))
    while q:
        li, dep = q.popleft()
        if dep == n+1:
            break
        if dep%2 == n%2:
            vcal = [li[i]*tenten[i] for i in range(len(nl))]
            ret = max(sum(vcal), ret)
        for i, j in combi:
            li[i], li[j] = li[j], li[i]
            if (tuple(li), (dep+1)%2) not in sets:
                sets.add((tuple(li), (dep+1)%2))
                q.append((li[:], dep+1))
            li[i], li[j] = li[j], li[i]
    return ret

for tc in range(1, int(input())+1):
    nl, n = input().rstrip().split() # 입
    nl, n = list(map(int, list(nl))), int(n) # 력
    print(f"#{tc} {큐사용()}")
