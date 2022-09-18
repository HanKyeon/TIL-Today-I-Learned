'''
사촌

첫 번 째 정수는 트리의 루트 노드.
루트의 자식.

1. 첫 번째 정수는 트리의 루트 노드이다.
2. 다음에 등장하는 연속된 수의 집합은 루트의 자식을 나타낸다. 이 집합에 포함되는 수의 첫 번째 수는 항상 루트 노드+1보다 크다.
3. 그 다음부터는 모든 연속된 수의 집합은 아직 자식이 없는 노드의 자식이 된다. 그러한 노드가 여러 가지 인 경우에는 가장 작은 수를 가지는 노드의 자식이 된다.
4. 집합은 수가 연속하지 않는 곳에서 구분된다.

입력
테케로 이루어짐.
노드n, 사촌구할 노드 k
n개의 수.
모든 수는 1보다 크거나 같고
100만 이하. 수열은 항상 증가. k는 항상 수열
종료는 0 0 제시

출력
k의 사촌 수 출력
'''
'''
from collections import deque
import sys
input = sys.stdin.readline

while True:
    n, k = map(int, input().rstrip().split())
    if not n and not k:
        break
    nl = deque(list(map(int, input().rstrip().split())))
    if n <= 4: # 사촌이 있으려면 노드가 5개 이상이어야 함.
        print(0)
        continue
    nod = [[], []] # 레벨 별 노드 그룹을 만들어서 저장 할 것
    nod[0] = [[nl.popleft()]] # 루트는 첫번째
    j, fla = 1, int(10e9) # j==레벨 fla == k가 나왔을 때 저장 할 레벨
    sav = [] # 연속된 숫자들을 임시 저장 할 리스트
    lnsum = 1 # 바로 윗 레벨의 노드 갯수.
    while nl: # 쭉 훑을 것
        x = nl.popleft()
        if not sav: # 비어있다면 임시저장시켜준다.
            sav.append(x)
            continue
        if sav[-1] + 1 == x: # 맨 뒤 값보다 1 크면 연속된 숫자들에 추가.
            sav.append(x)
            continue
        else: # 2이상 차이나면
            nod[j].append(sav) # j레벨에 연속된 숫자들을 넣어준다.
            if k in sav: # 연속된 숫자들 중 k가 있다면
                fla = j # 레벨 저장
            sav = [x] # 새로운 임시값
            if lnsum == len(nod[j]): # 바로 윗 레벨 노드 자식들을 다 채워줬다면
                lnsum = sum([len(i) for i in nod[j]]) # 레벨을 올려줌.
                nod.append([]) # 다음 노드 레벨 리스트 생성
                j += 1 # 레벨업!
                if j > fla: # 다음 레벨 갈 필요 없음.
                    break
    if k in sav: # 마지막에 k가 있다면
        fla = j # 레벨을 갱신해주고
    nod[j].append(sav) # 붙여준다.
    ans = 0
    for i in nod[fla]: # 그 레벨을 돌며
        if k in i: # 같은 부모는 패스
            continue
        ans += len(i) # 정답에 더해주기.
    if j < 2: # 레벨이 2 이상이어야 답이 나온다.
        ans = 0
    print(nod)
    print(ans)
'''
'''
3 5
1 3 5 7
3 5
1 3 5 6
'''

from sys import stdin

while True:
    n, k = map(int, stdin.readline().rstrip().split())
    if n == k == 0:
        break

    nodes = [-1]  # 인덱스 맞추기 위해 기본 노드 넣어줌
    nodes.extend(list(map(int, stdin.readline().rstrip().split())))
    depth = -1
    idx = 0
    group = [-1] * (n+1)  # 그룹으로 묶어주기

    for i in range(1, n+1):
        if nodes[i] == k:
            idx = i  # 사촌을 구해야하는 노드의 인덱스
            # print(f'idx: {idx}')
        if nodes[i] - nodes[i-1] != 1:  # 차이가 1 넘게 나면 depth 추가
            depth += 1
        group[i] = depth

    # print(group)  # [-1, 0, 1, 1, 1, 2, 2, 3, 4, 4, 4]

    c = 0
    grandparent = group[group[idx]]  # 할아버지 노드
    print(f'grandparent: {group[group[idx]]}') # 1
    print(f'parent: {group[idx]}') # 3
    for i in range(1, n+1):
        if group[i] != group[idx] and group[group[i]] == grandparent:
            c += 1
    print(group)
    print(nodes)
    print(c)


'''
import sys
input = sys.stdin.readline

while True:
    n,k = map(int,input().rstrip().split())
    if not n and not k:
        break
    a = [-1] + list(map(int,input().rstrip().split()))
    parent = [0]*(n+1)
    parent[0] = -1
    target = 0
    idx = -1
    for i in range(1,n+1):
        if a[i] == k:
            target = i
        if a[i] != a[i-1]+1:
            idx+=1
        parent[i] = idx
    answer = 0
    for i in range(1,n+1):
        if parent[i] != parent[target] and parent[parent[i]] == parent[parent[target]]:
            answer+=1
    print(answer)
'''
'''
from collections import deque
import sys
input = sys.stdin.readline

while True:
    n, k = map(int, input().rstrip().split())
    if not n and not k:
        break
    nl = deque(list(map(int, input().rstrip().split())))
    if n == 1 or n == 2:
        print(0)
        continue
    nod = [[], []]
    nod[0] = [[nl.popleft()]]
    j, fla = 1, 0
    sav = []
    lnsum = 1
    while nl:
        x = nl.popleft()
        if not sav:
            sav.append(x)
            continue
        if sav[-1] + 1 == x:
            sav.append(x)
            continue
        else:
            nod[j].append(sav)
            if k in sav:
                fla = j
            sav = [x]
            if lnsum == len(nod[j]):
                lnsum = sum([len(i) for i in nod[j]])
                nod.append([])
                j += 1
                if j > k:
                    break
    if k in sav:
        fla = j
    nod[j].append(sav)
    print(nod)
    ans = 0
    for i in nod[fla]:
        # print(*i)
        if k in i:
            continue
        ans += len(i)
    print(ans)

'''









